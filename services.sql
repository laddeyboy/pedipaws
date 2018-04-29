--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: appointment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.appointment (
    id integer NOT NULL,
    clientname character varying,
    petname character varying,
    service character varying,
    date date,
    start_time time without time zone,
    end_time time without time zone,
    email character varying,
    phone character varying,
    groomer_id integer,
    comment character varying
);


ALTER TABLE public.appointment OWNER TO postgres;

--
-- Name: appointment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.appointment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.appointment_id_seq OWNER TO postgres;

--
-- Name: appointment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.appointment_id_seq OWNED BY public.appointment.id;


--
-- Name: groomers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.groomers (
    id integer NOT NULL,
    groomer character varying,
    groomer_id integer
);


ALTER TABLE public.groomers OWNER TO postgres;

--
-- Name: groomers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.groomers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.groomers_id_seq OWNER TO postgres;

--
-- Name: groomers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.groomers_id_seq OWNED BY public.groomers.id;


--
-- Name: reviews; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reviews (
    id integer NOT NULL,
    name character varying,
    stars integer,
    text character varying
);


ALTER TABLE public.reviews OWNER TO postgres;

--
-- Name: reviews_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reviews_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reviews_id_seq OWNER TO postgres;

--
-- Name: reviews_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reviews_id_seq OWNED BY public.reviews.id;


--
-- Name: services; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.services (
    id integer NOT NULL,
    service character varying,
    description character varying,
    price integer,
    groomer character varying,
    duration integer
);


ALTER TABLE public.services OWNER TO postgres;

--
-- Name: services_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.services_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_id_seq OWNER TO postgres;

--
-- Name: services_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.services_id_seq OWNED BY public.services.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appointment ALTER COLUMN id SET DEFAULT nextval('public.appointment_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groomers ALTER COLUMN id SET DEFAULT nextval('public.groomers_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews ALTER COLUMN id SET DEFAULT nextval('public.reviews_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.services ALTER COLUMN id SET DEFAULT nextval('public.services_id_seq'::regclass);


--
-- Data for Name: appointment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.appointment (id, clientname, petname, service, date, start_time, end_time, email, phone, groomer_id, comment) FROM stdin;
1	Paul	Mittens	Black Tie Special	2018-05-04	15:00:00	16:00:00	paul@aol.com	281-567-9988	1	No eyeliner
\.


--
-- Name: appointment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.appointment_id_seq', 1, true);


--
-- Data for Name: groomers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.groomers (id, groomer, groomer_id) FROM stdin;
1	Aaron	1
\.


--
-- Name: groomers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.groomers_id_seq', 1, true);


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reviews (id, name, stars, text) FROM stdin;
1	Katy	4	Service was PURRfect!
2	Joey	5	My dog looks so suave, I think *I* need a makeover!
3	Jason	4	Loved it. Will recommend to all my friends!
4	Kelvin	5	My cat is a jerk, but now he is a good-looking jerk!
\.


--
-- Name: reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reviews_id_seq', 4, true);


--
-- Data for Name: services; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.services (id, service, description, price, groomer, duration) FROM stdin;
1	Black Tie Special	Styling, Blowout and Formal Attire. Outfit is yours to keep!	200	Aaron	60
2	Casual Friday	Haircut, Nail trim, and free sunglasses	50	Aaron	30
3	Sunday Best	Haircut, Styling, and Blowout	75	Aaron	45
4	Nail Trim - Cat/Small Dog	A Pedi for your Paws! Trim all nails	20	Aaron	15
5	Nail Trim - Dog	A Pedi for your Paws! Trim all nails	25	Aaron	20
6	Haircut	Basic Trim	30	Aaron	30
7	Summer Cut	Hot Summers mean cool coats. Full shave with optional shaping	45	Aaron	45
8	Wash	Gentle shampoo and blowdry	35	Aaron	20
9	Color treatment - Cat/Small Dog	Ethical dyes available to color pet coat	60	Aaron	45
10	Color treatment - Dog	Ethical dyes available to color pet coat	75	Aaron	60
\.


--
-- Name: services_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.services_id_seq', 10, true);


--
-- Name: appointment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pkey PRIMARY KEY (id);


--
-- Name: groomers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groomers
    ADD CONSTRAINT groomers_pkey PRIMARY KEY (id);


--
-- Name: reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (id);


--
-- Name: services_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

