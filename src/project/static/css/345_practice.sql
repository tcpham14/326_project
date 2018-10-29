create table B(

	c int,
	d int,
	primary key(c)

)

create table A(

	a int,
	b int,
	c int,
	d int,
	primary key(c) references B


)
