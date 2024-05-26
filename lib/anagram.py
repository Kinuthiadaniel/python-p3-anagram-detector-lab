# your code goes here!
class Anagram:
  def __init__(self, name):
    self.name = name

  def match(self, word_list):
    return ([w for w in word_list if self.is_anagram(w)])

  def is_anagram(self, candidate):
    candidate_lower = candidate.lower()
    return candidate_lower != self.name and sorted(candidate_lower) == sorted(self.name)
    