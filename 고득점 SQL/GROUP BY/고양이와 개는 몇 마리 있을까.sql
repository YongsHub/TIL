-- 코드를 입력하세요
(SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) as count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Cat')
UNION
(SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) as count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog');