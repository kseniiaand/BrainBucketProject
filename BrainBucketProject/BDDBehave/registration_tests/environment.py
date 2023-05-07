from BrainBucketProject.utils.config_reader import ConfigReader
from BrainBucketProject.webelements.browser import Browser

def before_all(context):
   configs = ConfigReader("BrainBucketProject/BDDBehave/registration_tests/steps/config.ini")
   context.configs = configs

def before_feature(context, feature):
   print('BEFORE FEATURE')

def before_scenario(context, scenario):
   configs = context.configs
   browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
   context.browser = browser

def after_scenario(context, scenario):
   context.browser.shutdown()

def after_feature(context, feature):
   print('AFTER FEATURE')

