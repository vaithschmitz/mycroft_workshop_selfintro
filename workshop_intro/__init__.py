from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests

class WorkshopSelfIntroSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(WorkshopSelfIntroSkill, self).__init__(name="WorkshopSelfIntroSkill")

        #   set state to avoid showing content multiple times
        self.already_had_tour = False
        self.already_had_background = False
        

    @intent_handler(IntentBuilder("").require("Hello")
    def handle_hello_intent(self, message):
        # will randomly speak one line from arg
        self.speak_dialog("hello")
        self.speak_dialog('intro')

    # hit API to get content on screen
    @intent_handler(IntentBuilder("").require("Tour")
    def handle_tour_intent(self, message):
        self.speak_dialog('confirm')

        # get content from db
        url ="someurl/content1"
        r=requests.get(url)
        json_output=r.json()
        output=json_output['data']
        events=output["Events"]

        # track content end and hit next intent
        # if already had background, go straight to portfolio
        if self.already_had_background:
            handle_portfolio_intent()
        else:
            self.speak('background.or.portfolio')
        


    @intent_handler(IntentBuilder("").require("Background")
    def handle_background_intent(self, message):
        self.speak_dialog("confirm")

        # get content from db
        url ="someurl/content1"
        r=requests.get(url)
        json_output=r.json()
        output=json_output['data']
        events=output["Events"]

        # track content end and hit next intent
        # if already had tour, go straight to portfolio
        if self.already_had_tour:
            handle_portfolio_intent()
        else:
            self.speak('tour.or.portfolio')
        

    @intent_handler(IntentBuilder("").require("Portfolio")
    def handle_portfolio_intent(self, message):
        self.speak_dialog("portfolio.confirm")

        # get content from db
        url ="someurl/content1"
        r=requests.get(url)
        json_output=r.json()
        output=json_output['data']
        events=output["Events"]

        # track content end, hit final message


    




    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return WorkshopSelfIntroSkill()
