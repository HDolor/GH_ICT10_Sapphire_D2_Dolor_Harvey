from pyscript import display
''' friends = {'E', 'A', 'A', 'N'}
friends.add('K')
friends.remove('N')
friends_checker = 'A' in friends
display(friends, target='out')

#Set operators
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
display(A|B, target='out') # display(A.union(B), target='out')
display(A&B, target='out') #intersect
display(A-B, target='out') #Difference
display(A^B, target='out')
display(A<=B, target='out')
display(A<B, target='out')
display(A>=B, target='out')
display(A>B, target='out')

video_games = frozenset(['TLoU', 'MH', 'Mc', 'Bl 3']) #frozenset
display(video_games, target='out') '''

V={'Aaron', 'Euan', 'Ishan', 'Vito', 'Seth'}
G={'Ishan', 'Mergal', 'Francesca', 'Seth'}
display(f'Students in atleast one club: ',(V|G), target='out0')
display(f'\nStudents in both clubs: ',(V&G), target='out1')
display(f'Students only in first club: ',(V-G), target='out2')
display(f'Students only in second club: ',(G-V), target='out3')
display(f'Students in exactly one club: ',(V^G), target='out4')