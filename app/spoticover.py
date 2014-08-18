import spotify
import threading
from PIL import Image
import os, os.path
from hashlib import md5

covers_directory = './cover/cover'
img_folder = 'cover/'

class SpotifyScavenger:
	"""docstring for SpotifyScavenger"""

	def __init__(self, login, password):

		self.login = login
		self.password = password
		self.session = spotify.Session()
		
		loop = spotify.EventLoop(self.session)
		loop.start()
		
		logged_in_event = threading.Event()
		def connection_state_listener(session):
		 	if session.connection.state is spotify.ConnectionState.LOGGED_IN:
		 		logged_in_event.set()

		self.session.on(
			spotify.SessionEvent.CONNECTION_STATE_UPDATED,
			connection_state_listener
			)

		print self.session.connection.state
		self.session.login(login, password)
		print self.session.connection.state
		logged_in_event.wait()
		print self.session.connection.state
		print self.session.user

	def login_session(self):
		session.login(User.login, User.password)
		logged_in_event.wait()
		return session		

	def get_user_toplist(self):
		toplist = self.session.get_toplist(
			type=spotify.ToplistType.TRACKS, 
			region=spotify.ToplistRegion.USER
			)
		toplist.load()
		return toplist

	def save_covers(self, toplist, covers_directory = './cover/cover'):
		i = 1
		for t in toplist.tracks:
			print i, t.name, t.duration // 1000, t.popularity
			album_uri = str(t.album).split('\'')[1].split('\'')[0]
			album = session.get_album(album_uri)
			album.load()
			cover = album.cover(spotify.ImageSize.LARGE) 
			cover.load()
			open(covers_directory + str(i) + '.jpg', 'w+').write(cover.data)
			i += 1



class CoversCollage:
	""" Generate uber cool cover images from a collection of images.
	"""

	FORMATS = {
		'poster': (1500, 1200, 300, 300),
		'facebook_cover':  (840, 280, 140, 140),
		'other_format': (1500, 1200, 90, 90),
	}

	def __init__(self, img_folder, format='poster'):
		self.width, self.heigth, self.width_thumbnail, self.height_thumbnail = self.FORMATS.get(format,
		                                        self.FORMATS['poster'])
		self.img_folder = img_folder
		self.format = format
		

	def make_picture(self):
		poster = Image.new('RGB', (self.width, self.heigth))
		n=1
		j=0
		for file in os.listdir(self.img_folder):
			while j < self.heigth:
				i=0
				while i < self.width:
					#opens an image:
					with Image.open(covers_directory + str(n) + ".jpg") as im_cover :
						print "cover" + str(n) +".jpg", im_cover.size
						im_cover.thumbnail((self.width_thumbnail, self.height_thumbnail))
						poster.paste(im_cover, (i,j))
					n += 1
					i += self.width_thumbnail
				j += self.height_thumbnail

		poster.save(self.format + ".jpg", "JPEG")
		#poster.show()	



if __name__ == '__main__':
	scavenger = SpotifyScavenger('', '')
	# toplist = scavenger.get_user_toplist()
	# scavenger.save_covers(toplist)
	cover = CoversCollage(img_folder, 'facebook_cover')
	print cover.format 

