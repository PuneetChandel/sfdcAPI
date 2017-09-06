import requests
import logging
from cachetools import LRUCache
from configuration.config import config

# log settings
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

cache = LRUCache(maxsize=4)

class login(object):
    @staticmethod
    def getSFToken(reset):
        if reset is True:
            resp = requests.post(
                config['settings']["loginUrl"] + "&client_id=" + config['settings']["clientId"] +
                "&client_secret=" + config['settings']["clientSecret"] + "&username="
                + config['settings']["userName"] + "&password=" + config['settings']["passWord"])

            if resp.status_code == 200:

                jsonresp = resp.json()
                logger.debug("ADDED TOKEN TO CACHE")
                cache["sfaccess_token"] = jsonresp["access_token"]
                cache["sfinstanceURL"] = jsonresp["instance_url"]
                logger.debug('Token : ' + jsonresp["access_token"])

                return jsonresp["access_token"], jsonresp["instance_url"]
            else:
                return {
                    "success": False
                }
        else:
            try:
                logger.debug("RETURNING FROM CACHE")
                return cache["sfaccess_token"], cache["sfinstanceURL"]
            except KeyError:
                resp = requests.post(
                    config['settings']["loginUrl"] + "&client_id=" + config['settings']["clientId"] + "&client_secret=" +
                    config['settings']["clientSecret"] + "&username=" + config['settings']["userName"] + "&password=" +
                    config['settings']["passWord"])

                if resp.status_code == 200:
                    jsonresp = resp.json()
                    logger.debug("ADDED TOKEN TO CACHE FOR FIRST TIME")
                    cache["sfaccess_token"] = jsonresp["access_token"]
                    cache["sfinstanceURL"] = jsonresp["instance_url"]
                    return jsonresp["access_token"], jsonresp["instance_url"]
                else:
                    return {
                        "success": False
                    }
