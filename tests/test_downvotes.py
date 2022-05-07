import unittest
from app.models import Pitch,User,Downvote


class DownvoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Collo = User(username = 'Collo', password = 'anything', email = 'collo@gm.com')
        self.new_pitch = Pitch(category = 'Promotion',title='Promotion',pitch='bla bla bla', user= self.user_Collo)
        self.new_downvote = Downvote(downvote_count=1,pitch=self.new_pitch,user= self.user_Collo)
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Downvote.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_downvote, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_downvote.downvote_count, 1)
        self.assertEquals(self.new_downvote.user, self.user_Collo)
        self.assertEquals(self.new_downvote.pitch, self.new_pitch)

    def test_save_downupvote(self):
        self.new_downvote.add_downvote()
        self.assertTrue(len(Downvote.query.all()) > 0)
        
    

       