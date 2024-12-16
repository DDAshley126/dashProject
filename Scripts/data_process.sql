alter table `user_behavior` add `Date` varchar(20);
alter table `user_behavior` add `Hour` int;
alter table `user_behavior` add `Minutes` int;
alter table `user_behavior` add `Seconds` int;
update `user_behavior` set Date=date(Timestamp);
update `user_behavior` set Hour=hour(Timestamp);
update `user_behavior` set Minutes=minute(Timestamp);

# 数据清洗
delete from `user_behavior` where Date < '2022-11-13' or Date > '2022-12-03';

# PV/UV
create table `average_view` (
	Date varchar(20),
	PV int,
	UV int,
	PV_UV_ratio decimal(10, 2)
);
insert into `average_view`(Date, PV, UV, PV_UV_ratio)
(select Date, count(*) as PV, count(distinct UserID) as UV, count(*)/count(distinct UserID) as PV_UV_ratio from `user_behavior`
group by Date);


# 用户活跃度分析
create table `user_activation` (
	Date varchar(20),
	Hour int,
	surf int,
	fav int,
	cart int,
	buy int
);
insert into `user_activation`
(select 
	Date, Hour, 
	sum(case when BehaviorType='pv' then 1 else 0 end) as surf,		# 浏览
	sum(case when BehaviorType='fav' then 1 else 0 end) as fav,		# 收藏
	sum(case when BehaviorType='cart' then 1 else 0 end) as cart,		# 加入购物车
	sum(case when BehaviorType='buy' then 1 else 0 end) as buy		# 下单购买
from `user_behavior`
group by Date, Hour
order by Date, Hour);


# 


