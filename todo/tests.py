from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo, Suggestions
import datetime
from .forms import TodoForm, SuggestionForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class TodoTest(TestCase):
    def setUp(self):
        self.userid=User(username='hien')
        self.todo=Todo(what='exercise', where='Mount Baker Park', when='2021-04-02', time='12:00:00', why='good health', how='30 minutes running', userid=self.userid)
        
    def test_string(self):
        self.assertEqual(str(self.todo), 'exercise')
        
    def test_tablename(self):
        self.assertEqual(str(Todo._meta.db_table), 'To Do List')



class SuggestionsTest(TestCase):
    def setUp(self):
        self.userid=User(username='user2')
        self.suggestions=Suggestions(suggestwhat='exercise', suggestwhere='Mount Baker Park', suggestwhen='2021-04-02', suggesttime='12:00:00', suggestwhy='good health', suggesthow='30 minutes running', userid=self.userid)
        
    def test_string(self):
        self.assertEqual(str(self.suggestions), 'exercise')
        
    def test_tablename(self):
        self.assertEqual(str(Suggestions._meta.db_table), 'Suggestions')

class NewTodoForm(TestCase):
       #valid form data
    def test_todoform(self):
        data={
               'what':'do exercise', 
               'where' :'Mount Baker Park', 
               'user':'hien', 
               'when': '2021-04-02',
               'time': '12:00:00',
               'why': 'good health',
               'how':'30 munites running'
            } 

        form=TodoForm (data)
        self.assertTrue(form.is_valid)

class NewSuggestion(TestCase):
       #valid form data
    def test_suggestionform(self):
        data={
               'suggestwhat':'do exercise', 
               'suggestwhere' :'Mount Baker Park', 
               'user':'hien', 
               'suggestwhen': '2021-04-02',
               'suggesttime': '12:00:00',
               'suggestwhy': 'good health',
               'suggesthow':'30 munites running'
            } 

        form=TodoForm (data)
        self.assertTrue(form.is_valid)

class New_Todolist_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='quyhoach712216')
        self.todo=Todo(what='exercise', where='Mount Baker Park', when='2021-04-02', time='12:00:00', why='good health', how='30 minutes running', userid=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newtodolist'))
        self.assertRedirects(response, '/accounts/login/?next=/todo/newtodolist/')

class New_Suggestions_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='quyhoach712216')
        self.suggestions=Suggestions(suggestwhat='exercise', suggestwhere='Mount Baker Park', suggestwhen='2021-04-02', suggesttime='12:00:00', suggestwhy='good health', suggesthow='30 minutes running', userid=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newsuggestion'))
        self.assertRedirects(response, '/accounts/login/?next=/todo/newsuggestion/')




    