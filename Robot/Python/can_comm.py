import can
import subprocess
import data
import threading
import math

class CAN_COMM:
	def __init__(self):
		subprocess.run(["sudo", "/sbin/ip", "link", "set", "can0","up", "type", "can", "bitrate", "500000"])
		subprocess.run(["sudo", "ip", "link", "set", "can0", "type", "can", "restart-ms", "500"])
		self.can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native
		data.running.set()
		self.thread = None

	def receive(self):
		while True:
			msg = self.can0.recv(10.0)
			
			if len(msg.data) == 4:
				enc1 = int(msg.data[1]<<8 | msg.data[0])
				enc2 = int(msg.data[3]<<8 | msg.data[2])

				if enc1 > 10000:
					enc1 -= 65535
				
				enc1 *= -1

				if enc2 > 10000:
					enc2 -= 65535

				data.enc_left = enc1
				data.enc_right = enc2

				x = data.x_current
				y = data.y_current
				f = data.f_current

				# Suma inkrimenta na levom i desnom enkoderu se ucitavaju

				encoder_left = data.enc_left
				encoder_right = data.enc_right
				#print(f"ENC1: {encoder_left} ENC2: {encoder_right}")

				# predjeni put u instanci vremena(trenutni)
				d = ((encoder_left + encoder_right) / 2) * \
					data.OdometryData.inc_mm  # inc_mm
				
				# ugao u instanci vremena
				g = -((encoder_left - encoder_right) / 2) * data.OdometryData.inc_deg

				# ukupan ugao
				f += g

				rad = math.radians(90 - f)

				# promena(diferencijal) x i y kordinate
				dx = -d * math.cos(rad)
				dy = d * math.sin(rad)

				# Trenutne kordinate posle promene
				x += dx
				y += dy

				# Trenutni ugao racuna
				if f < 0:
					f = abs(f) % 360
					f = -f

				else:
					f = f % 360

				# Nova trenutna pozicija
				data.x_current = x
				data.y_current = y
				data.f_current = f
				
				print(f"X: {x}, Y: {y}")

			if msg is None:
				print('Timeout occurred, no message.')

	def start(self):
		self.thread = threading.Thread(target=self.receive)
		self.thread.start

if __name__ == "__main__":
	comm = CAN_COMM()
	comm.receive()