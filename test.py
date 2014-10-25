

import time
import math

out = open('outfile.txt', 'w')
out.write('qwe\n-----\n qwe\n')
start = time.time()
print("2\n3\n5\n7\n11\n13\n17\n19\n23\n")
out.write( "2\n3\n5\n7\n11\n13\n17\n19\n23\n")
for i in range(29, 1000000, 2):
    if (
                                            i % 2 ==  0 or # |(                                                         )
                                            i % 3 ==  0 or # |(                                                         )
                                        i % 5 ==  0 or # |(                                                         )
                                    i % 7 ==  0 or # |(   ,                )
                                i % 11 == 0 or # |(                     )
                            i % 13 == 0 or # |(                                                         )
                        i % 17 == 0 or # |(                                                         )
                    i % 19 == 0 or # |(                                                         )
                i % 23 == 0    # |(                                                         )
    ):
        continue

    else:
        for j in range(29, int(math.sqrt(i) + 1), 2):
            if i % j == 0:
                break
        else:
            print(i)
            out.write(str(i) + "\n")

finish = time.time()
print(finish - start)
out.write('Program work at ' + str(finish - start) + ' second')
out.close()

