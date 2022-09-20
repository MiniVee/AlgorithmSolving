# https://school.programmers.co.kr/learn/courses/30/lessons/59044

# SELECT ANIMAL_INS.name, ANIMAL_INS.datetime
# from ANIMAL_INS
#
# left outer join ANIMAL_OUTS
#
# on ANIMAL_OUTS.animal_id = ANIMAL_ins.animal_id
#
# where ANIMAL_OUTS.name is null and ANIMAL_ins.name is not null
#
# order by ANIMAL_INS.datetime
#
# limit 3