import random

colours = {'white':'peace','red':'love','green':'nature','black':'evil','yellow':'positivity','blue':'sky',
			'orange':'attraction','beige':'calm','dark blue':'integrity','brown':'earth'}

# The quiz data. Keys are states and values are their capitals.



# Generate quiz files
for num in range(1):
    
    with open('colours%s.txt' % (num + 1), 'w') as file, \
            open('answers%s.txt' % (num + 1), 'w') as keyfile:

        present= list(colours.keys())
        random.shuffle(present)

        
        for question in range(5):
            correct = colours[present[question]]
            wrong = list(colours.values())
            del wrong[wrong.index(correct)]
            wrong= random.sample(wrong, 2)
            options = wrong + [correct]
            random.shuffle(options)

     
            file.write('%s. What is the indication of %s?\n' %
                           (question + 1, present[question]))
            for i in range(1):
                file.write('    %s. %s\n' % ('ABCD'[i], options[i]))
                file.write('\n')
                
                keyfile.write(
                    '%s. %s\n' % (
                        question + 3,
                        'ABCD'[options.index(correct)]   #answer key to the file
                    )
                )
