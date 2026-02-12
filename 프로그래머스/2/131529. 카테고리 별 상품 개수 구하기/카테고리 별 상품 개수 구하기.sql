SELECT 
    LEFT(PRODUCT_CODE, 2) AS CATEGORY, -- 앞 2글자 자르기
    COUNT(*) AS PRODUCTS              -- 개수 세기
FROM PRODUCT
GROUP BY CATEGORY               -- 자른 결과물(CATEGORY)로 뭉치기
ORDER BY CATEGORY ASC;              -- 카테고리 기준 오름차순