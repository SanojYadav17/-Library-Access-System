class Appliance:
    def status(self):
        print("Appliance works")
        
class Fan(Appliance):
    def status(self):
        print("Fan is spinning at full speed")
        
class Light(Appliance):
    def status(self):
        print("Light Glow")
        
class AC(Appliance):
    def status(self):
        print("AC is cooling at 25 degree celcious")
        
devices = [Fan(), Light(), AC()]

for device in devices:
    device.status()
