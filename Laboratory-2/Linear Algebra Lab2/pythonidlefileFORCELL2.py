def eagle_kinematics(s, t):
    req_shape = 4 #set the req_shape to 4 elements
    v = np.zeros((req_shape-1,)) #creates  [0,0,0,] from 4 zeros to minus 1
    a = np.zeros((req_shape-2,)) #creates  [0,0,] from 4 zeros to minus 2
    t_vect = np.array([t**3, t**2, t, 1]) #raises the number to 3 annd 2 and print that number and the 1 in array
    if s.shape == (req_shape,): #then s.shape here is checking the number of array if it is equal to req_shape which is EQUAL
        v = np.array([3*s[0],2*s[1], s[2]]) #we got [6 2 3]
        a = np.array([2*v[0],v[1]])         #we got [12   2]
        s_t = np.sum(np.multiply(s, t_vect)) #we got 28 , # when we print only "t_vect" I got [8 4 2 1]
        v_t = np.sum(np.multiply(v, t_vect[1:])) # we got 31,  # when we print only "t_vect[1:]" I got [4 2 1]
        a_t = np.sum(np.multiply(a, t_vect[2:])) # I got 26, #when i print only "t_vect[1:]" I got [2 1]
        
    else:
        print(f'Input displacement vector is not valid. Make sure that the vector shape is ({req_shape},)')
    
    return s_t, v_t, a_t #If I remove this, I will not get the (28, 31, 26)


x = np.array([2,1,3,2]) #getting error of t is not defined when i removed the t = 2 and run
t = 2 #when i try to run the funtionn without the x : and only t, i am getting an error x is not defines
eagle_kinematics(x, t)

#printing it all results to (28, 31, 26)


--------------------------------renamed version----------------------------------------------
def eagle_kinematics(velocity, eagle_time):
    req_shape = 4 #set the req_shape to 4 elements
    shape3 = np.zeros((req_shape-1,)) #creates  [0,0,0,] from 4 zeros to minus 1
    shape2 = np.zeros((req_shape-2,)) #creates  [0,0,] from 4 zeros to minus 2
    eagle_time = np.array([t**3, t**2, t, 1]) #raises the number to 3 annd 2 and print that number and the 1 in array | ERROR WHEN t IS NOT DECLARED
    if velocity.shape == (req_shape,): #then s.shape here is checking the number of array if it is equal to req_shape which is EQUAL
        velocity2 = np.array([3*velocity1[0],2*velocity1[1], velocity1[2]]) #we got [6 2 3]
        velocity3 = np.array([2*velocity2[0],velocity2[1]])         #we got [12   2]
        dist_total1 = np.sum(np.multiply(velocity1, eagle_time)) ; #we got 28 , | when we print only "t_vect" I got [8 4 2 1] |   print(s) I got [2 1 3 2]
        dist_total2 = np.sum(np.multiply(velocity2, eagle_time[1:]));# we got 31,  | when we print only "t_vect[1:]" I got [4 2 1] |    print(v) I got [6 2 3]
        dist_total3 = np.sum(np.multiply(velocity3, eagle_time[2:])); # I got 26, | when i print only "t_vect[1:]" I got [2 1] |    print(a) [12  2]
        
    else:
        print(f'Input displacement vector is not valid. Make sure that the vector shape is ({req_shape},)')
    
    return dist_total1, dist_total2, dist_total3 #If I remove this, I will not get the (28, 31, 26) - no result
--------------------------------------------------------
velocity1 = np.array([2,1,3,2]) #getting error of t is not defined when i removed the t = 2 and run
t = 2 #when i try to run the funtionn without the x : and only t, i am getting an error x is not defines
eagle_kinematics(velocity1, eagle_time)

#printing it all results to (28, 31, 26)
