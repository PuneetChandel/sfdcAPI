#!/usr/bin/env python3

import logging
from flask import jsonify, Flask, Response
from utils.sfServiceMgr import sfServiceMgr
import os
import json
from jsonschema import validate, ValidationError
app = Flask(__name__)
from configuration.config import config

# log settings
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))


class sfobject(object):
        @staticmethod
        def createsfobj(sfdata,oname):

            if oname in config["settings"]["objectstovaliadte"]:
                data_path = os.path.join(project_path, 'schema/'+oname+'.json')
                schema = open(data_path).read()

                try:
                    validate(sfdata, json.loads(schema))
                except ValidationError as e:
                    resp = jsonify({"errorcode": "ValidationErrror", "message": e.message})
                    resp.status_code = 400
                    return resp

            if len(sfdata)==1:
                sfresp = sfServiceMgr.sfPost(sfdata[0],oname)
            else:
                sfreqData=[]
                ref=0
                for r in sfdata:
                    ref+=1
                    r["attributes"]={"type":oname,"referenceId": str(ref)}
                    sfreqData.append(r)
                sfcompdata={"records" :sfreqData}
                sfresp= sfServiceMgr.sfPostComposite(sfcompdata,oname)

            if sfresp.status_code == 201:
                resp=jsonify(sfresp.json())
                resp.status_code = 201
                return resp
            elif sfresp.status_code == 401:
                resp = jsonify(
                    {"code": "401",
                     "message": "Authentication failure"
                     })
                resp.status_code = sfresp.status_code
                return resp
            elif sfresp.status_code == 400:
                resp = jsonify(sfresp.json())
                resp.status_code = 400
                return resp
            else:
                resp = jsonify(
                    {"code": "500",
                     "message": "Internal server Error"
                     })
                resp.status_code = sfresp.status_code
                return resp

        @staticmethod
        def getobj(id,oname):
            sfresp = sfServiceMgr.sfget(id,oname)
            if sfresp.status_code == 200:
                resp = jsonify(sfresp.json())
                resp.status_code = 200
                return resp
            elif sfresp.status_code == 401:
                resp = jsonify(
                    {"code": "401",
                     "message": "Authentication failure"
                     })
                resp.status_code = sfresp.status_code
                return resp
            else:
                resp = jsonify(
                    {"code": "500",
                     "message": "Internal server Error"
                     })
                resp.status_code = sfresp.status_code
                return resp

        @staticmethod
        def updateobj(sfreqData,id,oname):
            sfresp = sfServiceMgr.sfPatch(sfreqData,id,oname)
            if sfresp.status_code == 204:
                resp = Response({
                    "success": True
                })
                resp.status_code = 204
                return resp
            elif sfresp.status_code == 401:
                resp = jsonify(
                    {"code": "401",
                     "message": "Authentication failure"
                     })
                resp.status_code = sfresp.status_code
                return resp
            else:
                resp = jsonify(
                    {"code": "500",
                     "message": "Internal server Error"
                     })
                resp.status_code = sfresp.status_code
                return resp



