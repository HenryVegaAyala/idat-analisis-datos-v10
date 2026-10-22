import matplotlib.pyplot as plt

canales = ['Facebook', 'Instagram', 'Twitter']
ventas = [350, 250, 150]

plt.pie(ventas, labels=canales, autopct="%1.5f%%")
plt.show()