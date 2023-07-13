import matplotlib.pyplot as plt

Years = [2010, 2011, 2012, 2013,  2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
Temperature  = [25.3, 27.1, 24.8, 26.5, 22.9, 23.7, 25.2, 26.8, 24.5, 23.9, 26.1, 28.3]

i = 0
x = 0
h = Temperature[0]
l = Temperature[0]

while i<len(Temperature):
    x+= Temperature[i]
    if Temperature[i]>h:
        h = Temperature[i]
   
    if Temperature[i]<l:
        l = Temperature[i]
    i+=1

print(x/len(Temperature)) 
print(h)
print(l)

plt.plot(Years, Temperature, marker = 'o', linestyle = '--', color = 'green')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature variations')
plt.show()
