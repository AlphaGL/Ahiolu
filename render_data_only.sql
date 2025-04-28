--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Debian 16.8-1.pgdg120+1)
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	main	locationcategory
7	main	productrating
8	main	products
9	main	servicerating
10	main	services
11	users	customuser
12	cities_light	country
13	cities_light	region
14	cities_light	city
15	cities_light	subregion
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add location category	6	add_locationcategory
22	Can change location category	6	change_locationcategory
23	Can delete location category	6	delete_locationcategory
24	Can view location category	6	view_locationcategory
25	Can add product rating	7	add_productrating
26	Can change product rating	7	change_productrating
27	Can delete product rating	7	delete_productrating
28	Can view product rating	7	view_productrating
29	Can add products	8	add_products
30	Can change products	8	change_products
31	Can delete products	8	delete_products
32	Can view products	8	view_products
33	Can add service rating	9	add_servicerating
34	Can change service rating	9	change_servicerating
35	Can delete service rating	9	delete_servicerating
36	Can view service rating	9	view_servicerating
37	Can add services	10	add_services
38	Can change services	10	change_services
39	Can delete services	10	delete_services
40	Can view services	10	view_services
41	Can add user	11	add_customuser
42	Can change user	11	change_customuser
43	Can delete user	11	delete_customuser
44	Can view user	11	view_customuser
45	Can add country	12	add_country
46	Can change country	12	change_country
47	Can delete country	12	delete_country
48	Can view country	12	view_country
49	Can add region/state	13	add_region
50	Can change region/state	13	change_region
51	Can delete region/state	13	delete_region
52	Can view region/state	13	view_region
53	Can add city	14	add_city
54	Can change city	14	change_city
55	Can delete city	14	delete_city
56	Can view city	14	view_city
57	Can add SubRegion	15	add_subregion
58	Can change SubRegion	15	change_subregion
59	Can delete SubRegion	15	delete_subregion
60	Can view SubRegion	15	view_subregion
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: cities_light_country; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.cities_light_country (id, name_ascii, slug, geoname_id, alternate_names, name, code2, code3, continent, tld, phone) FROM stdin;
\.


--
-- Data for Name: cities_light_region; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.cities_light_region (id, name_ascii, slug, geoname_id, alternate_names, name, display_name, geoname_code, country_id) FROM stdin;
\.


--
-- Data for Name: cities_light_subregion; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.cities_light_subregion (id, name, name_ascii, slug, geoname_id, alternate_names, display_name, geoname_code, country_id, region_id) FROM stdin;
\.


--
-- Data for Name: cities_light_city; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.cities_light_city (id, name_ascii, slug, geoname_id, alternate_names, name, display_name, search_names, latitude, longitude, region_id, country_id, population, feature_code, timezone, subregion_id) FROM stdin;
\.


--
-- Data for Name: users_customuser; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.users_customuser (id, password, last_login, is_superuser, is_staff, is_active, date_joined, email, first_name, last_name, phone, profile) FROM stdin;
8	pbkdf2_sha256$870000$aaJrddGol7o1vjmWcK9qh5$qkKFu9igedJQY22aXyosB4ekur/y8tEZlxOUV4AhseQ=	2025-04-16 13:04:53.363303+00	f	f	t	2025-04-16 13:04:05.938669+00	ikefrancise9@gmail.com	Francise	Ikechukwu	07019552183	
10	pbkdf2_sha256$870000$wD2V16avQ60vAjUxuOTagV$uJz2y5Fav1D/WvrMhE8YbSEECz/IEcshNFysz/JKieE=	2025-04-17 09:55:40.454747+00	f	f	t	2025-04-17 09:54:35.908082+00	chimamkpamstanley90@gmail.com	Chinetugo	Chimamkpam	08069600677	
5	pbkdf2_sha256$870000$T20OwvsqudJPjYEjYpvNns$YpUM4xy+4hDwDY2wZDGTBshElznsxlowZ8LDQ/vYEdA=	2025-04-17 10:11:52.250458+00	f	f	t	2025-04-15 18:58:44.435086+00	Nimechenationalsf@gmail.com	NIMechE	NIMechE	07038772855	
1	pbkdf2_sha256$870000$IeBfnPexsiTYM2PxpdsyDr$tt5K4KzlbykX8lidTZFtzQYVLVAc41Hcmylnr/I0ExA=	2025-04-18 12:56:07.386895+00	t	t	t	2025-04-07 18:37:24+00	ichukwugozirim@gmail.com	Chukwugozirim	Ibeawuchi	08138582078	image/upload/v1744730519/s7uwg9741sjjxli4qdmt.jpg
11	pbkdf2_sha256$870000$b2YSq1t5CZQIqndqNK4mki$U5CZwkXZn471Zm1YUhaUmF4xF4jaOOKLphMl+SmjDx4=	2025-04-24 16:25:40.854533+00	f	f	t	2025-04-24 16:25:01.531047+00	ambitionpromise5@gmail.com	Promise	Anyanwu	08142943193	
12	pbkdf2_sha256$870000$1nXPIjpJduJeJiHLk0D3od$jeePXk1vDr/UqKkgTCA7lJYoSrE2CeRQYuuwWYJCSPw=	\N	f	f	t	2025-04-25 08:00:12.939172+00	chrischike@gmail.com	Chikere	Nwachukwu	08060423353	
13	pbkdf2_sha256$870000$n2NjNCcmbwBmzMxLnDayfg$PlhEnmdey2LVZjo3FaC6FNKHjjVKi4DKFaaFH76XdWM=	2025-04-27 06:25:35.320482+00	f	f	t	2025-04-27 06:24:32.559153+00	chibuikedesmond53@gmail.com	Chibyke	Ventures	08162166147	
6	pbkdf2_sha256$870000$E1c2f2Nj4fx8YiR2iiLaeI$mijWCvJTN8NyK/DFTqptuJSVuunwUx2zO/SiH3ftmGU=	\N	f	f	t	2025-04-16 12:19:11.569439+00	Ikechu1998@gmail.com	Francise	Ikechukwu	07040563804	
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
18	2025-04-16 13:13:06.184312+00	7	nnekaogochukwu246@gmail.com	3		11	1
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-04-07 17:29:57.75774+00
2	contenttypes	0002_remove_content_type_name	2025-04-07 17:29:59.393204+00
3	auth	0001_initial	2025-04-07 17:30:06.975082+00
4	auth	0002_alter_permission_name_max_length	2025-04-07 17:30:08.200608+00
5	auth	0003_alter_user_email_max_length	2025-04-07 17:30:08.963743+00
6	auth	0004_alter_user_username_opts	2025-04-07 17:30:10.689267+00
7	auth	0005_alter_user_last_login_null	2025-04-07 17:30:12.712685+00
8	auth	0006_require_contenttypes_0002	2025-04-07 17:30:13.938594+00
9	auth	0007_alter_validators_add_error_messages	2025-04-07 17:30:15.281924+00
10	auth	0008_alter_user_username_max_length	2025-04-07 17:30:16.618372+00
11	auth	0009_alter_user_last_name_max_length	2025-04-07 17:30:17.958621+00
12	auth	0010_alter_group_name_max_length	2025-04-07 17:30:20.284274+00
13	auth	0011_update_proxy_permissions	2025-04-07 17:30:21.009639+00
14	auth	0012_alter_user_first_name_max_length	2025-04-07 17:30:22.252227+00
15	users	0001_initial	2025-04-07 17:30:32.264101+00
16	admin	0001_initial	2025-04-07 17:30:35.644757+00
17	admin	0002_logentry_remove_auto_add	2025-04-07 17:30:36.310317+00
18	admin	0003_logentry_add_action_flag_choices	2025-04-07 17:30:37.33712+00
19	cities_light	0001_initial	2025-04-07 17:30:49.469911+00
20	cities_light	0002_city	2025-04-07 17:30:56.94321+00
21	cities_light	0003_auto_20141120_0342	2025-04-07 17:30:57.46419+00
22	cities_light	0004_autoslug_update	2025-04-07 17:30:58.636234+00
23	cities_light	0005_blank_phone	2025-04-07 17:31:00.978087+00
24	cities_light	0006_compensate_for_0003_bytestring_bug	2025-04-07 17:31:02.297148+00
25	cities_light	0007_make_country_name_not_unique	2025-04-07 17:31:05.566843+00
26	cities_light	0008_city_timezone	2025-04-07 17:31:08.61675+00
27	cities_light	0009_add_subregion	2025-04-07 17:31:16.60387+00
28	cities_light	0010_auto_20200508_1851	2025-04-07 17:31:23.154746+00
29	cities_light	0011_alter_city_country_alter_city_region_and_more	2025-04-07 17:31:24.018765+00
30	main	0001_initial	2025-04-07 17:31:28.294294+00
31	main	0002_initial	2025-04-07 17:31:34.545481+00
32	main	0003_remove_services_other_service_d_and_more	2025-04-07 17:31:37.108353+00
33	main	0004_products_is_paid_services_is_paid	2025-04-07 17:31:39.950009+00
34	main	0005_locationcategory_status_products_product_status_and_more	2025-04-07 17:31:43.743064+00
35	main	0006_productrating_user_name_servicerating_user_name	2025-04-07 17:31:46.298899+00
36	main	0007_products_user_services_user	2025-04-07 17:31:50.601741+00
37	main	0008_alter_products_user_alter_services_user	2025-04-07 17:31:55.194402+00
38	main	0009_alter_products_user_alter_services_user	2025-04-07 17:32:00.122435+00
39	main	0010_alter_locationcategory_category_and_more	2025-04-07 17:32:00.992102+00
40	main	0011_alter_locationcategory_category_and_more	2025-04-07 17:32:03.802139+00
41	main	0012_alter_locationcategory_category_and_more	2025-04-07 17:32:04.67507+00
42	main	0013_alter_locationcategory_category_and_more	2025-04-07 17:32:05.806314+00
43	main	0014_alter_locationcategory_category_and_more	2025-04-07 17:32:07.057925+00
44	main	0015_products_is_promoted_products_promotion_fee_and_more	2025-04-07 17:32:11.796016+00
45	sessions	0001_initial	2025-04-07 17:32:14.455132+00
46	users	0002_alter_customuser_managers_alter_customuser_groups_and_more	2025-04-07 17:32:15.145433+00
47	users	0003_alter_customuser_email	2025-04-07 17:32:17.01928+00
48	main	0002_alter_products_product_image_and_more	2025-04-08 18:20:47.547333+00
49	users	0004_customuser_profile	2025-04-10 01:53:49.130325+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
t6u8w5jjsytqqg4u53me2q7n3r1ldnfu	.eJxVizsOwjAQBe-yNYq8jj8bSiRquIG1XttyBAQpJhXi7hCUAso38-YJgZdHDUvLcxgT7AFh98siyyVPq1hn675mg6073ni8nuZzvU_5sD3_8sqtftqcdPEDJsw2qiJEAxtL0QkrrXspRdlIbDwpdkyeNQqJcX1Eg86QgtcbkXo3HA:1u4h5O:HkvYe2FHFhpVoqcDmL8l2mGnrSUnhBbkdeBpMd4Td-4	2025-04-29 14:16:26.871699+00
jp1hk94tlbb7zjekrbzc8zz6xiok68wi	.eJxVizsOwjAQBe_iGkX-e02JRA03iNbrtRwBiRSTCnF3EpQCyjfz5iV6XJ61XxrP_ZDFUThx-GUJ6cbjJrbZuq_ZYevODxzul_lap5FP-_Mvr9jq2uZEVllQkiDEjA4pFU0QfXRkdU5FesMMzIGZV2e0txqcgaCK1EaJ9weijjfC:1u4lXf:EYyt8pgMe3MaIMq1zQCb8JVCx4xCChuFeQlM1FnjBKg	2025-04-29 19:01:55.092808+00
9f89wo66ep5nwcninffug51dfrf8zem1	.eJxVizsOwjAQBe-yNYq8jj8bSiRquIG1XttyBAQpJhXi7hCUAso38-YJgZdHDUvLcxgT7AFh98siyyVPq1hn675mg6073ni8nuZzvU_5sD3_8sqtftqcdPEDJsw2qiJEAxtL0QkrrXspRdlIbDwpdkyeNQqJcX1Eg86QgtcbkXo3HA:1u5007:5VmA6-H6xmUYo0-C9zZBCjVcJaO3-4d-TlIfSKoGFG8	2025-04-30 10:28:15.402511+00
0ytlxieeb8q0o10joggwzn7m7wj1rxkh	.eJxVizsOwjAQBe-yNYq8jj8bSiRquIG1XttyBAQpJhXi7hCUAso38-YJgZdHDUvLcxgT7AFh98siyyVPq1hn675mg6073ni8nuZzvU_5sD3_8sqtftqcdPEDJsw2qiJEAxtL0QkrrXspRdlIbDwpdkyeNQqJcX1Eg86QgtcbkXo3HA:1u2Fmv:iaufaf0BkyJKSS4jaD4plpdRtI2H8RZ0lYStlewti5k	2025-04-22 20:43:17.723156+00
whsbwcnfqj7ofu4brjjz9sdk7qj97309	.eJxVizsOwjAQBe-yNYrsWF57KZGo4QbWrj9yBAQpJhXK3UNQCijfzJs3BJ5fNcwtT2FIcAQPh18mHG953MQ2W_c1O2zd-cHD_TJd63PMp_35l1du9dMmTZFij1axTiLaluKkVxKNJXZSCFlQOSzGoLLkSXnUGUWsT-iMhmUFjJw3BA:1u52RY:OOUfn1KmiQwxX-SRU3YUz9ow6SjhiOXwzzZ8Vcyt2nU	2025-04-30 13:04:44.396083+00
jfsr6zpn8vkka44l3jy2zfh2i7k9f87h	.eJxVizsOwjAQBe-yNYrsWF57KZGo4QbWrj9yBAQpJhXK3UNQCijfzJs3BJ5fNcwtT2FIcAQPh18mHG953MQ2W_c1O2zd-cHD_TJd63PMp_35l1du9dMmTZFij1axTiLaluKkVxKNJXZSCFlQOSzGoLLkSXnUGUWsT-iMhmUFjJw3BA:1u52Rb:pP5NuFLpV0lfpnvZN7vItElnNdWkBBX6dTV7L5C18-E	2025-04-30 13:04:47.387565+00
2z8giz8xi946sm86rhe600o9s5604qog	.eJxVizsOwjAQBe-yNYrsWF57KZGo4QbWrj9yBAQpJhXK3UNQCijfzJs3BJ5fNcwtT2FIcAQPh18mHG953MQ2W_c1O2zd-cHD_TJd63PMp_35l1du9dMmTZFij1axTiLaluKkVxKNJXZSCFlQOSzGoLLkSXnUGUWsT-iMhmUFjJw3BA:1u52Re:syKCQ5cv4CGAm6EoZsLQjsTAguVjzKKAmxtH83oPU2Y	2025-04-30 13:04:50.47906+00
hsjk56twhoyhlnvr02491pgh612q26p0	.eJxVizsOwjAQBe_iGkVe_6FEoiY3sHbttRwBiRSTCuXuEJQCyjfz5iUiLs8al8ZzHLI4CSUOv4ww3XjcxDZb9zU7bN3lgcP9Ovd1Gvm8P__yiq1-Wu_QJpUtGECXPFkKlClolQnASAk5cNGQWAUlMdhjQjbae3TFIfgi1jeC0Tdy:1u2SWn:FueuOCL63rxiV9o9JfH3Dp9oK6k4pYspaeNK7jArOao	2025-04-23 10:19:29.562885+00
3xbg4wjgwglsrltcrb17d5kyzossg1z6	.eJxVizsOwjAQBe-yNYrsWF57KZGo4QbWrj9yBAQpJhXK3UNQCijfzJs3BJ5fNcwtT2FIcAQPh18mHG953MQ2W_c1O2zd-cHD_TJd63PMp_35l1du9dMmTZFij1axTiLaluKkVxKNJXZSCFlQOSzGoLLkSXnUGUWsT-iMhmUFjJw3BA:1u52Rh:OHJya62PUqPLIlMd-MJlwo7a1VIK5D7XU5cKt5LtrSA	2025-04-30 13:04:53.396202+00
ugkkfs9be0xx0bhpuyw4gs3l8xb3h1yy	.eJxVizsOwjAQBe_iGkVe_6FEoiY3sHbttRwBiRSTCuXuEJQCyjfz5iUiLs8al8ZzHLI4CSUOv4ww3XjcxDZb9zU7bN3lgcP9Ovd1Gvm8P__yiq1-Wu_QJpUtGECXPFkKlClolQnASAk5cNGQWAUlMdhjQjbae3TFIfgi1jeC0Tdy:1u2UEN:bMJ_RaXClI7T9keiMy90T-jELq_TSLNKmuEyyGs3nJQ	2025-04-23 12:08:35.62745+00
avrgr3bx7bi475xq24lxo3gsu5mg48li	.eJxVizsOwjAQBe_iGkVe_6FEoiY3sHbttRwBiRSTCuXuEJQCyjfz5iUiLs8al8ZzHLI4CSUOv4ww3XjcxDZb9zU7bN3lgcP9Ovd1Gvm8P__yiq1-Wu_QJpUtGECXPFkKlClolQnASAk5cNGQWAUlMdhjQjbae3TFIfgi1jeC0Tdy:1u2ZUS:IuSYtsxwPxEkGZl9pB1XokZpi7OXfrAGJ7BtX-uG610	2025-04-23 17:45:32.584714+00
kyx9vbmwfj1j4dcalxn3z5oo23bk6bco	.eJxVizsOwjAQBe_iGkV2sv4sJRI13MBae9dyBAQpJhXi7hCUAso38-apIi2PGpcmcxxZ7RWq3S9LlC8yrWKdrfuaDbbueKPxeprP9T7JYXv-5ZVa_bQmi05o7FBMZssENvVsLLOWUAaP6BAggaaeQYNHl0ORgDlpD0nEqdcbjcY3lg:1u52Sj:uWP7JcK8q6cfkhdIrsVPQwsBkWLskpbHmYidw3QyjRA	2025-04-30 13:05:57.608035+00
2jlc2xwq9i3nmisx2l3h7f15eptz560y	.eJxVizEOwjAMRe-SGVVug9OEEYkZbhDZjqtUQJEaOiHuToo6wPjff-9lIi3PHJeicxyTOZgWzO4XMslVp_VZZ2m-zwZLc7rTeDvPl_yY9LiZf3mmkmvbscM-tM5bIBFQsMrIISCnCryD3ltyIh6rR8qK-wE7HtTbgJTEvD-d7zfs:1u5Ly5:TFaEYjj9AApfKcpcfPHfzFYIj3f2-x5T8o0ISL8sZt4	2025-05-01 09:55:37.468911+00
mk53swixege0fuhikg7kdbzzv97nnzv4	.eJxVizEOwjAMRe-SGVVug9OEEYkZbhDZjqtUQJEaOiHuToo6wPjff-9lIi3PHJeicxyTOZgWzO4XMslVp_VZZ2m-zwZLc7rTeDvPl_yY9LiZf3mmkmvbscM-tM5bIBFQsMrIISCnCryD3ltyIh6rR8qK-wE7HtTbgJTEvD-d7zfs:1u5Ly8:ZZdl18nTepcligqbmloEWzm-jnWcMDCD5lcRJayZUPg	2025-05-01 09:55:40.501634+00
ib4xsewd2x6w19679syjcsemp8o02uvb	.eJxVizEOwjAMRe-SGVUlbnDCiMRMbxA5jq1UQJEaOlXcHYo6wPjf-28xkeZniXOVKQ7ZHA2Y3S9LxFcZV7HO2nzNBmtzvtNwu0x9eYxy2p5_eaFaPq3m0ErGPbHzCuwUrQPoEDhkL9Z3QkKomhIgJyWnrdjgLJEgcziY1xuqRDi5:1u2hiu:0m9uiJBdin5yPVwX2ZafaHCjwAHIb9_v0_EMQZ_MHik	2025-04-24 02:33:00.904433+00
86qg5mzqjy0lbzeg4dmxkpgo4e75kx3w	.eJxVizsOwjAQBe-yNYq8jj8bSiRquIG1XttyBAQpJhXi7hCUAso38-YJgZdHDUvLcxgT7AFh98siyyVPq1hn675mg6073ni8nuZzvU_5sD3_8sqtftqcdPEDJsw2qiJEAxtL0QkrrXspRdlIbDwpdkyeNQqJcX1Eg86QgtcbkXo3HA:1u5lGJ:eJaUL0XWnUGX5BZLIfeR1PXbm8mb2nsMmdI6LgJeoiU	2025-05-02 12:56:07.418266+00
xeqlwasub4ulna8p50x7jugj2jiadlcf	.eJxVizsOwjAQBe_iGkVe2-u1KZGo4QbW-idHQJBiUiHuDkEpoHwzb54i8PJoYellDmMWewEgdr8wcrqUaTXr7MPXbLAPxxuP19N8bvepHLbnX964t09rKaes0JONKiPXaixi1Z6zwWqQFUAyrjpPXiqCSjoZltJDkux0JPF6A59rNwI:1u7zOO:tCaC6uU4k8rkyX-gHqEIleqiO2d9VN4XcL0QR96ZR0Y	2025-05-08 16:25:40.891575+00
iuo64r6nnlg8v7hdqqfhd9feykn0g311	.eJxVizEOwjAMRe-SGVUlbnDCiMRMbxA5jq1UQJEaOlXcHYo6wPjf-28xkeZniXOVKQ7ZHA2Y3S9LxFcZV7HO2nzNBmtzvtNwu0x9eYxy2p5_eaFaPq3m0ErGPbHzCuwUrQPoEDhkL9Z3QkKomhIgJyWnrdjgLJEgcziY1xuqRDi5:1u2qlb:VXhVRc4AldGjnMkEwWUOKWXqSfRbv-EQHHwB3FNrXtE	2025-04-24 12:12:23.834913+00
d014mgw7m8s7opurg451qwlwjszf0rjd	.eJxVizEOwjAMRe-SGVVxQ9yYEakz3CBybUupgCI1dELcHYo6wPjf--_pMi-Pkpdqcx7VHRwEt_uFA8vFptWsszZfs8Ha9Dcer6f5XO6THbfnX164lk8bzQJqUiRRs444CiJwxFbBIFGUlki8TzxwBPMgSmlvg2foUEJwrze45je9:1u8vSJ:yCODUtupCzNyb-EeN-JJzg1Dz1vN1szixhqu08YHd4c	2025-05-11 06:25:35.354847+00
\.


--
-- Data for Name: main_locationcategory; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.main_locationcategory (id, category, country, state, city, status) FROM stdin;
\.


--
-- Data for Name: main_products; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.main_products (id, product_name, product_image, product_description, product_price, product_category, product_country, product_state, product_city, product_brand, product_provider_phone, is_paid, product_status, user_id, is_promoted, promotion_fee) FROM stdin;
4	R134a, Gas and Oil	image/upload/v1744745059/r46ffsujahi7vibq8pdd.jpg	R134a refrigerant	10000	automotive	NG	Imo	Owerri	Gas and Oil	07038772855	t	published	5	t	1000
5	R134a, Gas and Oil	image/upload/v1744745188/v0uymx5voazgd4cp8rtt.jpg	R134a refrigerant	10000	automotive	NG	Imo	Owerri	Gas and Oil	07038772855	f	pending	5	t	1000
6	Es350 smart key	image/upload/v1744884074/mhebzyfmf1igi3ohfm40.jpg	Works on your es350 2007 - 2009 model	75000	automotive	NG	All	All	Lexus/ toyota	08069600677	f	pending	10	t	1000
7	Es350 smart key	image/upload/v1744884079/vk3jhfim8ilm81a5txxb.jpg	Works on your es350 2007 - 2009 model	75000	automotive	NG	All	All	Lexus/ toyota	08069600677	f	pending	10	t	1000
8	Es350 smart key	image/upload/v1744884162/g3anzadvoukhb2e9lnp4.jpg	Works on your es350 2007 - 2009 model	75000	automotive	NG	All	All	Lexus/ toyota	08069600677	t	published	10	t	1000
9	A/C parts	image/upload/v1745736752/xdyovbvnd8iavbhmeca4.jpg	Direct Belgium	85000	automobile	NG	Imo	Owerri	Chibyke	08162166147	f	pending	13	t	1000
\.


--
-- Data for Name: main_productrating; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.main_productrating (id, rating, review, created_at, user_id, product_id, user_name) FROM stdin;
1	5.0	Very precise, \r\nThanks for your services.	2025-04-17 10:13:12.331423+00	5	8	anonymous
\.


--
-- Data for Name: main_services; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.main_services (id, service_name, service_image, service_description, service_category, service_country, service_state, service_city, service_provider_name, service_provider_expertise, service_provider_experience_year, service_provider_email, service_provider_phone, other_service_a, other_service_b, other_service_c, is_paid, service_status, user_id, is_promoted, promotion_fee) FROM stdin;
7	Automobile Electrician	image/upload/v1744810075/fzzatq7c4dramsc3ecnf.jpg	Auto Electrical and diagnostic Services	all	NG	Imo	Owerri	Ikechukwu Francis onwuka	Auto Elect	5	Ikechu1998@gmail.com	07040563804	Diagnosis	Scanning	Automobile Air Condition	f	pending	8	t	1000
8	Automobile Electrician	image/upload/v1744810079/y1ztvaymvqa7c29gker9.jpg	Auto Electrical and diagnostic Services	all	NG	Imo	Owerri	Ikechukwu Francis onwuka	Auto Elect	5	Ikechu1998@gmail.com	07040563804	Diagnosis	Scanning	Automobile Air Condition	f	pending	8	t	1000
9	Automobile Electrician	image/upload/v1744810091/ywnivksduqhfzzmvlrsz.jpg	Auto Electrical and diagnostic Services	all	NG	Imo	Owerri	Ikechukwu Francis onwuka	Auto Elect	5	Ikechu1998@gmail.com	07040563804	Diagnosis	Scanning	Automobile Air Condition	f	pending	8	f	1000
10	Automobile Electrician	image/upload/v1744810101/zsew53auqrssl5xvruwg.jpg	Auto Electrical and diagnostic Services	all	NG	Imo	Owerri	Ikechukwu Francis onwuka	Auto Elect	5	Ikechu1998@gmail.com	07040563804	Diagnosis	Scanning	Automobile Air Condition	f	pending	8	t	1000
11	Automobile Electrician	image/upload/v1744810307/emnhntkoii182puljete.jpg	Auto Electrical and Diagnosis	automobile	NG	All	All	Ikechukwu Francis onwuka	Auto Elect	5	Ikechu1998@gmail.com	07040563804	Automobile Air condition	Automobile Diagnostic services	\N	t	published	8	f	1000
12	Iyke AirCon	image/upload/v1744821917/bwrxoipnfeaerriqdr7y.jpg	Automobile air condition repair	automobile	NG	Imo	Owerri	Chimamkpam George Ikechukwu	Auto AirCon	12	Engnrgeorgeiyke@gmail.com	07038772855	Automobile Programming	Automobile diagnosis	\N	f	pending	5	t	1000
13	Promise	image/upload/v1745512943/wc8vbkw6ld2d5ztaww6q.jpg	Automobile Electrician	automobiles	NG	All	Owerri	Promise Elect	Electrical and electrical	7	ambitionpromise5@gmail.com	08142943193	Automobile repairs	Automobile sales	\N	t	published	11	t	1000
\.


--
-- Data for Name: main_servicerating; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.main_servicerating (id, rating, review, created_at, user_id, service_id, user_name) FROM stdin;
2	5.0	Top notch ≡ƒæî	2025-04-16 13:39:18.615211+00	5	11	anonymous
\.


--
-- Data for Name: users_customuser_groups; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.users_customuser_groups (id, customuser_id, group_id) FROM stdin;
\.


--
-- Data for Name: users_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: bconnect_db_user
--

COPY public.users_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);


--
-- Name: cities_light_city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.cities_light_city_id_seq', 1, false);


--
-- Name: cities_light_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.cities_light_country_id_seq', 1, false);


--
-- Name: cities_light_region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.cities_light_region_id_seq', 1, false);


--
-- Name: cities_light_subregion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.cities_light_subregion_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 18, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 49, true);


--
-- Name: main_locationcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.main_locationcategory_id_seq', 1, false);


--
-- Name: main_productrating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.main_productrating_id_seq', 1, true);


--
-- Name: main_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.main_products_id_seq', 9, true);


--
-- Name: main_servicerating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.main_servicerating_id_seq', 2, true);


--
-- Name: main_services_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.main_services_id_seq', 13, true);


--
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.users_customuser_groups_id_seq', 1, false);


--
-- Name: users_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.users_customuser_id_seq', 13, true);


--
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bconnect_db_user
--

SELECT pg_catalog.setval('public.users_customuser_user_permissions_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

