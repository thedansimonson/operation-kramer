# operation-kramer
Python script for Ras Pi to play sound effects on motion sensor.

Nothing fancy here, mostly posting for my own records.

Called operation-kramer because I did it originally with Seinfeld scene transition sounds.


## Run configuration
I recommend shelling in and running with screen, if you want to put it somewhere hidden.

Ideally, put the sounds in one folder. It doesn't search recursively.

Call it with:

    $ python play_on_motion.py path_to_sounds 3600

The second argument is how long to force wait between play; in this case, one hour, so it
doesn't get annoying.


