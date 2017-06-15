ThinkPython
===========

LaTeX source, code examples, and exercise solutions for Think Python, 2nd edition, by Allen Downey.
#program1( ex 1.2thinkpy allendowney )

#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
#mile) in minutes and seconds? What is your average speed in miles per hour?

#main( )

#inputs

kilom             = 0.0    #   want  floating point for these
miles             = 0.0


in_mins           = 0      # 'how long you took in mins and seconds?'
in_secs           = 0


#intermediate values

total_sec_time    = 0.0
total_hr_time     = 0.0
avg_pace          = 0.0
avg_speed         = 0.0


#outputs

out_mins          = 0
out_secs          = 0

#from math import*
#data scipy and numpy and LIGO data https://losc.ligo.org/data/
#get wavelab
#get pywavelets


#in_func( )   #computes the time taken to run the race in secs, one could also write an input function taking values from keyboard

in_mins = 42
in_secs = 42

total_sec_time =  60*in_mins + in_secs

total_hr_time  =  total_sec_time / (60*60)



#pace_calc( ): computes

#   average pace == total time taken / distance ran

#   units:  seconds per mile

kilom = 10

miles = kilom/1.62

avg_pace = total_sec_time /  miles


#pace_convert( ): converts the average pace from units of seconds per mile to units of [mins and secs] per mile

out_mins = avg_pace // 60     #integer division in Pyth, this is the minutes part

out_secs = avg_pace % 60      #this is the seconds part

out_secs = out_secs // 1      # only display int seconds



#pace_out( ):

space = '    '

print (space, 'You ran ' ,miles, ' miles in', in_mins, 'minutes and ', in_secs,' seconds\n' )

print(space , 'Your average pace was \n ' )

print(space, out_mins, ' minutes and ',  out_secs, ' seconds per mile : ) \n')


#speed_calc( ):  computes

#    average speed ==  distance ran / total time taken ==  (1 / av pace)

#    units:  miles per second

avg_speed = 1.0 / avg_pace




#speed_convert( ): converts the average speed from units of miles per second to units of miles per hour

avg_speed = avg_speed * 60 *60

#avg_speed = avg_speed // 1.0                                    #one way to chop off a decimal part




#speed_out( ):

print (space,"that's an average " , "{:.2f}".format(avg_speed), 'miles per hour\n')            # use of dec place formatting




