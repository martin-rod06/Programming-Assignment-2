import unittest
import data
import hw2


class MyTestCase(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        rectangle = hw2.create_rectangle(data.Point(10, 10), data.Point(2, 2))
        self.assertEqual(rectangle, 'Rectangle(Point(2, 10), Point(10, 2))')

    def test_create_rectangle2(self):
        rectangle = hw2.create_rectangle(data.Point(10, 10), data.Point(2, 2))
        self.assertNotEqual(rectangle, 'Rectangle(Point(10, 2), Point(2, 10))')

    # Part 2
    def test_shorter_duration_than1(self):
        duration1 = data.Duration(5, 20)
        duration2 = data.Duration(5, 21)
        self.assertTrue(hw2.shorter_duration_than(duration1, duration2))

    def test_shorter_duration_than2(self):
        duration1 = data.Duration(5, 20)
        duration2 = data.Duration(5, 21)
        self.assertFalse(hw2.shorter_duration_than( duration2, duration1))

    # Part 3
    def test_songs_shorter_than(self):
        songs = [data.Song('Artist', 'Title', data.Duration(3, 21)), data.Song('JAKE', 'Songs', data.Duration(5, 30)),
                 data.Song('Tom', "Tom's Song", data.Duration(5, 9))]
        self.assertEqual(hw2.songs_shorter_than(songs,data.Duration(5, 0)),[data.Song('Artist', 'Title', data.Duration(3, 21))])

    def test_songs_shorter_than2(self):
        songs = [data.Song('Artist', 'Title', data.Duration(3, 21)), data.Song('JAKE', 'Songs', data.Duration(5, 30)),
                 data.Song('Tom', "Tom's Song", data.Duration(5, 9))]
        self.assertNotEqual(hw2.songs_shorter_than(songs,data.Duration(5, 0)), [data.Song('JAKE', 'Songs', data.Duration(5, 30)), data.Song('Tom', "Tom's Song", data.Duration(5, 9))])
    # Part 4

    def test_running_time1(self):
        songs = [data.Song('Artist', 'Title', data.Duration(3, 21)), data.Song('JAKE', 'Songs', data.Duration(5, 30)),
                 data.Song('Tom', "Tom's Song", data.Duration(5, 9))]
        self.assertEqual(hw2.running_time(songs, [1, 1, 1]), data.Duration(16, 30))

    def test_running_time2(self):
        songs = [data.Song('Artist', 'Title', data.Duration(3, 21)), data.Song('JAKE', 'Songs', data.Duration(5, 30)),
                 data.Song('Tom', "Tom's Song", data.Duration(5, 9))]
        self.assertNotEqual(hw2.running_time(songs, [1, 1, 1]), data.Duration(15, 90))
    # Part 5
    def test_validate_route1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        self.assertTrue(hw2.validate_route(city_links,['san luis obispo', 'santa margarita', 'atascadero']))

    def test_validate_route1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        self.assertFalse(hw2.validate_route(city_links, ['san luis obispo', 'atascadero']))
    # Part 6

    def test_longest_repetition(self):
        repetition = [1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 1]
        self.assertEqual(hw2.longest_repetition(repetition), 8)

    def test_longest_repetition2(self):
        repetition = [1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 1]
        self.assertNotEqual(hw2.longest_repetition(repetition), 2)


if __name__ == '__main__':
    unittest.main()
