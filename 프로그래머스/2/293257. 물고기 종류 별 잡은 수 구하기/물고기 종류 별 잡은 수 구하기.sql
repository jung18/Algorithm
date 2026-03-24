select count(FI.ID) as FISH_COUNT, FISH_NAME
from FISH_INFO as FI join FISH_NAME_INFO as FN
on FI.FISH_TYPE = FN.FISH_TYPE
group by FISH_NAME
order by FISH_COUNT desc;
