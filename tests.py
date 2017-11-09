
import os
from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from flask import *
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean

from app.models import *


class tests(TestCase):

# -----------
# Test Artists
# -----------
	
	# Test that table "Artists" is writable
	def test_write_artists(self):
		query = session.query(Artists).all()
		startSize = len(query)

		session.add(Artists(name = 'ARTIST', genre = 'GENRE'))
		session.commit()
		query = session.query(Artists).all()
		endSize = len(query)
		
		self.assertEqual(startSize + 1, endSize)


	# Test that table "Artists" can be written multiple queries 
	def test_write_artist_multiple(self):
		query = session.query(Artists).all()
		startSize = len(query)

		session.add(Artists(name = 'ARTIST_MULTIPLE_1', genre = 'GENRE'))
		session.add(Artists(name = 'ARTIST_MULTIPLE_2', genre = 'GENRE'))
		session.commit()
		query = session.query(Artists).all()
		endSize = len(query)

		self.assertEqual(startSize + 2, endSize)

	
	# Test that table "Artists" is readable
	def test_read_artists(self):
		session.add(Artists(name = 'TESTREAD', genre = 'GENRE'))
		session.commit()

		query = session.query(Artists).all()
		found = False

		for artist in query:
			if(artist.name == 'TESTREAD' and artist.genre == 'GENRE'):
				found = True

		self.assertTrue(found)

	
	# Test that table "Artists" is readable and accounts for case sensitivity
	def test_read_artists_case_sensitive(self):
		session.add(Artists(name = 'TESTCASE', genre = 'GENRE'))
		session.commit()

		query = session.query(Artists).all()
		found = False

		for artist in query:
			if(artist.name == 'TESTCASE'):
				found = True
			if(artist.name == 'testcase'):
				found = False

		self.assertTrue(found)

	
	# Test filtering "Artists" by an attribute
	def test_read_artists_atribute(self):
		session.add(Artists(name = 'TESTATTR', genre = 'Alternative-Rock'))
		session.commit()

		query = session.query(Artists).filter(Artists.name == 'TESTATTR').first()

		self.assertTrue(query is not None)
		self.assertTrue(query.genre == 'Alternative-Rock')

	
	# Test filtering "Artists" by an attribute returns multiple unique results
	def test_read_artists_atribute_multiple(self):
		session.add(Artists(name = 'TESTATTR1', genre = 'Electronic'))
		session.add(Artists(name = 'TESTATTR2', genre = 'Electronic'))
		session.commit()

		query = session.query(Artists).filter(Artists.genre == 'Electronic').all()

		self.assertTrue(query is not None)
		self.assertTrue(len(query) == 2)

		genres = []
		for artist in query:
			genres.append(Artists.genre)

		self.assertTrue(genres[0] == genres[1])

	
	# Test deletion of a row in table "Artists"
	def test_artists_delete(self):
		session.add(Artists(name = 'ARTISTDEL'))
		session.commit()

		query = session.query(Artists).filter(Artists.name == 'ARTISTDEL').first()

		self.assertTrue(query is not None)

		session.delete(query)
		session.commit()
	
		new_query = session.query(Artists).filter(Artists.name == 'ARTISTDEL').first()
		self.assertTrue(new_query is None)


# -----------
# Test Albums
# -----------

	# Test that table "Albums" is writable
	def test_write_albums(self):
		query = session.query(Albums).all()
		startSize = len(query)

		session.add(Albums(name = 'ALBUM', genre = 'GENRE'))
		session.commit()
		query = session.query(Albums).all()
		endSize = len(query)
		
		self.assertEqual(startSize + 1, endSize)


	# Test that table "Albums" can be written multiple queries 
	def test_write_albums_multiple(self):
		query = session.query(Albums).all()
		startSize = len(query)

		session.add(Albums(name = 'ALBUM_MULTIPLE_1', genre = 'GENRE'))
		session.add(Albums(name = 'ALBUM_MULTIPLE_2', genre = 'GENRE'))
		session.commit()
		query = session.query(Albums).all()
		endSize = len(query)

		self.assertEqual(startSize + 2, endSize)


	# Test that table "Albums" is readable
	def test_read_albums(self):
		session.add(Albums(name = 'TESTREAD', genre = 'GENRE'))
		session.commit()

		query = session.query(Albums).all()
		found = False

		for album in query:
			if(album.name == 'TESTREAD' and album.genre == 'GENRE'):
				found = True

		self.assertTrue(found)


	# Test that table "Albums" is readable and accounts for case sensitivity
	def test_read_albums_case_sensitive(self):
		session.add(Albums(name = 'TESTCASE', genre = 'GENRE'))
		session.commit()

		query = session.query(Albums).all()
		found = False

		for album in query:
			if(album.name == 'TESTCASE'):
				found = True
			if(album.name == 'testcase'):
				found = False

		self.assertTrue(found)


	# Test filtering "Albums" by an attribute
	def test_read_albums_atribute(self):
		session.add(Albums(name = 'TESTATTR', genre = 'Alternative-Rock'))
		session.commit()

		query = session.query(Albums).filter(Albums.name == 'TESTATTR').first()

		self.assertTrue(query is not None)
		self.assertTrue(query.genre == 'Alternative-Rock')

	
	# Test filtering "Albums" by an attribute returns multiple unique results
	def test_read_albums_atribute_multiple(self):
		session.add(Albums(name = 'TESTATTR1', genre = 'Electronic'))
		session.add(Albums(name = 'TESTATTR2', genre = 'Electronic'))
		session.commit()

		query = session.query(Albums).filter(Albums.genre == 'Electronic').all()

		self.assertTrue(query is not None)
		self.assertTrue(len(query) == 2)

		genres = []
		for album in query:
			genres.append(Albums.genre)

		self.assertTrue(genres[0] == genres[1])

	
	# Test deletion of a row in table "Albums"
	def test_albums_delete(self):
		session.add(Albums(name = 'ARTISTDEL'))
		session.commit()

		query = session.query(Albums).filter(Albums.name == 'ARTISTDEL').first()

		self.assertTrue(query is not None)

		session.delete(query)
		session.commit()
	
		new_query = session.query(Albums).filter(Albums.name == 'ARTISTDEL').first()
		self.assertTrue(new_query is None)


# -----------
# Test Songs
# -----------

	# Test that table "Songs" is writable
	def test_write_songs(self):
		query = session.query(Songs).all()
		startSize = len(query)

		session.add(Songs(name = 'SONG', genre = 'GENRE'))
		session.commit()
		query = session.query(Songs).all()
		endSize = len(query)
		
		self.assertEqual(startSize + 1, endSize)


	# Test that table "Songs" can be written multiple queries 
	def test_write_songs_multiple(self):
		query = session.query(Songs).all()
		startSize = len(query)

		session.add(Songs(name = 'SONG_MULTIPLE_1', genre = 'GENRE'))
		session.add(Songs(name = 'SONG_MULTIPLE_2', genre = 'GENRE'))
		session.commit()
		query = session.query(Songs).all()
		endSize = len(query)

		self.assertEqual(startSize + 2, endSize)



if __name__ == "__main__":
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	main()