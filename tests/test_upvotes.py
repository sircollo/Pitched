import unittest
from app.models import Pitch,User,Upvote


class UpvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Collo = User(username = 'Collo', password = 'anything', email = 'collo@gm.com')
        self.new_pitch = Pitch(category = 'Promotion',title='Promotion',pitch='bla bla bla', user= self.user_Collo)
        self.new_upvote = Upvote(upvote_count=21,pitch=self.new_pitch,user= self.user_Collo) 
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Upvote.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_upvote, Upvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_upvote.upvote_count, 21)
        self.assertEquals(self.new_upvote.user, self.user_Collo)
        self.assertEquals(self.new_upvote.pitch, self.new_pitch)

    def test_save_downupvote(self):
        self.new_upvote.add_upvote()
        self.assertTrue(len(Upvote.query.all()) > 0)
        
    

       