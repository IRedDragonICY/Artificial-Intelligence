# Program aktivitas 1
from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
suka = Relation()
facts(suka, ("ellen", "tenis"),
      ("john", "football"),
      ("john", "tenis"),
      ("mary", "renang"),
      ("tom", "tenis"),
      ("tom", "basket"),
      ("eric", "renang"),
      ("mary", "tenis"))
x = var()
tom_hobbies = run(0, x, suka("tom", x))
print("Tom: ", tom_hobbies)