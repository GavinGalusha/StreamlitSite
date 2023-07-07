

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
name = 'Pikachu'
#name = input("enter input")
query = "Python Turtle code for " + name
 
for j in search(query, tld="co.in", num=3, stop=3, pause=2):
    print(j)