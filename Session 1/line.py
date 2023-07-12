import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013,  2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
temperature  = [25.3, 27.1, 24.8, 26.5, 22.9, 23.7, 25.2, 26.8, 24.5, 23.9, 26.1, 28.3]

i = 0
x = 0
h = temperature[0]
l = temperature[0]

while i<len(temperature):
    x+= temperature[i]
    if temperature[i]>h:
        h = temperature[i]
   
    if temperature[i]<l:
        l = temperature[i]
    i+=1

print(x/len(temperature)) 
print(h)
print(l)

plt.plot(years, temperature, marker = 'o', linestyle = '--', color = 'green')
plt.xlabel('year')
plt.ylabel('temperature')
plt.title('temperature variations')
plt.show()
