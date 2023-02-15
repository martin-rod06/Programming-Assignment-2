import data

# Write your functions for each part in the space below.
# Part 1


def create_rectangle(Point1 : data.Point, Point2:data.Point)-> data.Rectangle:
    topleftpoint = data.Point(0, 0)
    bottomrightpoint = data.Point(0, 0)
    if Point1.x < Point2.x:
        topleftpoint.x = Point1.x
    else:
        topleftpoint.x = Point2.x
    if Point1.y > Point2.y:
        topleftpoint.y = Point1.y
    else:
        topleftpoint.y = Point2.y
    if Point1.x > Point2.x:
        bottomrightpoint.x = Point1.x
    else:
        bottomrightpoint.x = Point2.x
    if Point1.y < Point2.y:
        bottomrightpoint.y = Point1.y
    else:
        bottomrightpoint.y = Point2.y
    return repr(data.Rectangle(topleftpoint, bottomrightpoint))


# Part 2
def shorter_duration_than(len1: data.Duration, len2: data.Duration) -> bool:
    if len1.minutes < len2.minutes:
        return True
    elif len1.minutes > len2.minutes:
        return False
    elif len1.seconds < len2.seconds:
        return True
    else:
        return False


# Part 3
def songs_shorter_than(songs: list[data.Song], duration: data.Duration)-> list[data.Song]:
    list_of_songs = []
    for song in songs:
        if song.duration.minutes < duration.minutes :
            list_of_songs.append(song)
        elif song.duration.minutes > duration.minutes:
            pass
        elif song. duration.seconds < duration.seconds:
            list_of_songs.append(song)
        else:
            pass
    return list_of_songs


# Part 4
def running_time(songs: list[data.Song], playlist: list[int] ) -> data.Duration:
    all_time = data.Duration(0,0)
    for position in playlist:
        if position < 0 or position > len(songs) - 1:
            pass
        else:
            all_time.minutes = all_time.minutes + songs[position].duration.minutes
            all_time.seconds = all_time.seconds + songs[position].duration.seconds
        if all_time.seconds >= 60:
            all_time.seconds = all_time.seconds - 60
            all_time.minutes= all_time.minutes + 1
    return all_time


# Part 5
def validate_route(city_links: list[list[str]], inquiry: list[str]) -> bool:
    if len(inquiry) == 0 or 1:
        for k in range(len(inquiry)):
            if k - 1 == -1:
                pass
            else:
                if list((inquiry[k], inquiry[k-1])) in city_links or list((inquiry[k-1], inquiry[k])) in city_links:
                    return True
                else:
                    return False


# Part 6
def longest_repetition(numbers: list[int]):
    max_rep = 0
    repetitions = 0
    for index in range(len(numbers)):
        if numbers[index - 1] == numbers[index]:
            repetitions = repetitions + 1
        else:
            repetitions = 0
        if max_rep < repetitions:
            max_rep = repetitions
            index_holder = index - max_rep
    return index_holder


