class Device:
    def __init__(self, device_id, manufacturer):
        self.device_id = device_id
        self.manufacturer = manufacturer
    def get_device_info(self):
        return f"Device ID: {self.device_id}, Manufacturer: {self.manufacturer}"
class Flyer:
    def fly(self):
        return "Dron is Flying......"
class Drone(Device, Flyer):
    def __init__(self, device_id, manufacturer, camera_resolution):
        super().__init__(device_id, manufacturer)
        self.camera_resolution = camera_resolution
    def capture_image(self):
        return f"Image Captured at {self.camera_resolution} resolution."
    def get_full_info(self):
        return f"{self.get_device_info()}, Camera: {self.camera_resolution}"

drone1 = Drone("DR575", "AeroTech", "6k")

print(drone1.get_device_info())
print(drone1.fly())
print(drone1.capture_image())
print(drone1.get_full_info())
