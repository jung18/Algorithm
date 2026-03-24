select FI.ID, FN.FISH_NAME, FI.LENGTH
from FISH_INFO as FI
join FISH_NAME_INFO as FN
on FI.FISH_TYPE = FN.FISH_TYPE
where (FI.FISH_TYPE, FI.LENGTH) in (
    select FISH_TYPE, max(LENGTH)
    from FISH_INFO
    group by FISH_TYPE
)
order by FI.ID;