from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('9zz14Prg2NuRnvaKKfsS7KQhBWZjotwru2M9ZJ8Dv2fJ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/87da8875-8bc5-4728-b1bd-d3dc7292787d')

def english_to_french(text1):
    """
    This function translates english to french
    """
    
    frenchtranslation = language_translator.translate(
        text=text1,
        model_id='en-fr'
    ).get_result()
    
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(text1):
    """
    This function translates french to english
    """
    
    englishtranslation = language_translator.translate(
        text=text1,
        model_id='fr-en'
    ).get_result()
    
    return englishtranslation.get("translations")[0].get("translation")
