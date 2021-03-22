from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo, Suggestions
import datetime
from .forms import TodoForm, SuggestionForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
