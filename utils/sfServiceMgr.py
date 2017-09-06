import requests
from utils.login import login
import logging.handlers
from configuration.config import config
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(config['settings']["logfilename"],
                                               maxBytes=config['settings']["logmaxBytes"],
                                               backupCount=config['settings']["logbackupCount"])

logger.addHandler(handler)

class sfServiceMgr(object):
    @staticmethod
    def sfPost(sfreqData, objectName):
        token, instanceURL = login.getSFToken(False)
        sfresp = requests.post(instanceURL + "/services/data/v39.0/sobjects/" + objectName,
                               json=sfreqData,
                               headers={"Authorization": "Bearer " + token})

        if sfresp.status_code == 401:
            logger.debug("UNAUTHORIZED ERROR")
            token, instanceURL = login.getSFToken(True)
            sfresp = requests.post(instanceURL + "/services/data/v39.0/sobjects/" + objectName,
                                   json=sfreqData,
                                   headers={"Authorization": "Bearer " + token})
        return sfresp

    @staticmethod
    def sfQuery(sfquery):
        token, instanceURL = login.getSFToken(False)

        sfresp = requests.get(instanceURL + "/services/data/v39.0/query/?q=" + sfquery,
                              headers={"Authorization": "Bearer " + token})

        if sfresp.status_code == 401:
            logger.debug("UNAUTHORIZED ERROR")
            token, instanceURL = login.getSFToken("True")
            sfresp = requests.get(instanceURL + "/services/data/v39.0/query/?q=" + sfquery,
                                  headers={"Authorization": "Bearer " + token})
        return sfresp

    @staticmethod
    def sfPatch(sfreqData,id,objectName):
        token, instanceURL = login.getSFToken(False)

        sfresp = requests.patch(instanceURL + "/services/data/v39.0/sobjects/" + objectName + "/" + id,
                                json=sfreqData,
                                headers={"Authorization": "Bearer " + token})

        if sfresp.status_code == 401:
            logger.debug("UNAUTHORIZED ERROR")
            token, instanceURL = login.getSFToken(True)
            sfresp = requests.patch(instanceURL + "/services/data/v39.0/sobjects/" + objectName + "/" + id,
                                    json=sfreqData,
                                    headers={"Authorization": "Bearer " + token})

        return sfresp

    @staticmethod
    def sfget(id,objectName):

        token, instanceURL = login.getSFToken(False)

        sfresp = requests.get(instanceURL + "/services/data/v39.0/sobjects/"+objectName+"/"+ id,
                              headers={"Authorization": "Bearer " + token})

        if sfresp.status_code == 401:
            logger.debug("UNAUTHORIZED ERROR")
            token, instanceURL = login.getSFToken(True)
            sfresp = requests.get(instanceURL + "/services/data/v39.0/sobjects/" + objectName + "/" + id,
                                  headers={"Authorization": "Bearer " + token})
        return sfresp


    @staticmethod
    def sfPostComposite(sfreqData,objectName):
        token, instanceURL = login.getSFToken('False')
        sfresp = requests.post(instanceURL + "/services/data/v39.0/composite/tree/"+ objectName,
                               json=sfreqData,
                               headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})

        if sfresp.status_code == 401:
            logger.debug("UNAUTHORIZED ERROR")
            token, instanceURL = login.getSFToken("True")
            sfresp = requests.post(instanceURL + "/services/data/v39.0/composite/tree/" + objectName,
                                   json=sfreqData,
                                   headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})

        return sfresp



