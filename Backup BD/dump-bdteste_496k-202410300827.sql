--
-- PostgreSQL database dump
--

-- Dumped from database version 12.19
-- Dumped by pg_dump version 15.3

-- Started on 2024-10-30 08:27:00

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 35 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: bdteste_496k_user
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO bdteste_496k_user;

--
-- TOC entry 4538 (class 0 OID 0)
-- Dependencies: 35
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: bdteste_496k_user
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 237 (class 1259 OID 19195)
-- Name: TabUsuarios; Type: TABLE; Schema: public; Owner: bdteste_496k_user
--

CREATE TABLE public."TabUsuarios" (
    "idUsuario" integer NOT NULL,
    codigo character varying(50) NOT NULL,
    nome character varying(100) NOT NULL
);


ALTER TABLE public."TabUsuarios" OWNER TO bdteste_496k_user;

--
-- TOC entry 236 (class 1259 OID 19193)
-- Name: TabUsuarios_idUsuario_seq; Type: SEQUENCE; Schema: public; Owner: bdteste_496k_user
--

CREATE SEQUENCE public."TabUsuarios_idUsuario_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."TabUsuarios_idUsuario_seq" OWNER TO bdteste_496k_user;

--
-- TOC entry 4540 (class 0 OID 0)
-- Dependencies: 236
-- Name: TabUsuarios_idUsuario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bdteste_496k_user
--

ALTER SEQUENCE public."TabUsuarios_idUsuario_seq" OWNED BY public."TabUsuarios"."idUsuario";


--
-- TOC entry 239 (class 1259 OID 19203)
-- Name: funcionario; Type: TABLE; Schema: public; Owner: bdteste_496k_user
--

CREATE TABLE public.funcionario (
    _id integer NOT NULL,
    nome character varying(50),
    email character varying(100)
);


ALTER TABLE public.funcionario OWNER TO bdteste_496k_user;

--
-- TOC entry 238 (class 1259 OID 19201)
-- Name: funcionario__id_seq; Type: SEQUENCE; Schema: public; Owner: bdteste_496k_user
--

CREATE SEQUENCE public.funcionario__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.funcionario__id_seq OWNER TO bdteste_496k_user;

--
-- TOC entry 4541 (class 0 OID 0)
-- Dependencies: 238
-- Name: funcionario__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bdteste_496k_user
--

ALTER SEQUENCE public.funcionario__id_seq OWNED BY public.funcionario._id;


--
-- TOC entry 241 (class 1259 OID 19211)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: bdteste_496k_user
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nome character varying(50) NOT NULL,
    email character varying(50) NOT NULL
);


ALTER TABLE public.usuarios OWNER TO bdteste_496k_user;

--
-- TOC entry 240 (class 1259 OID 19209)
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: bdteste_496k_user
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuarios_id_seq OWNER TO bdteste_496k_user;

--
-- TOC entry 4542 (class 0 OID 0)
-- Dependencies: 240
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bdteste_496k_user
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- TOC entry 4390 (class 2604 OID 19198)
-- Name: TabUsuarios idUsuario; Type: DEFAULT; Schema: public; Owner: bdteste_496k_user
--

ALTER TABLE ONLY public."TabUsuarios" ALTER COLUMN "idUsuario" SET DEFAULT nextval('public."TabUsuarios_idUsuario_seq"'::regclass);


--
-- TOC entry 4391 (class 2604 OID 19206)
-- Name: funcionario _id; Type: DEFAULT; Schema: public; Owner: bdteste_496k_user
--

ALTER TABLE ONLY public.funcionario ALTER COLUMN _id SET DEFAULT nextval('public.funcionario__id_seq'::regclass);


--
-- TOC entry 4392 (class 2604 OID 19214)
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: bdteste_496k_user
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- TOC entry 4528 (class 0 OID 19195)
-- Dependencies: 237
-- Data for Name: TabUsuarios; Type: TABLE DATA; Schema: public; Owner: bdteste_496k_user
--

INSERT INTO public."TabUsuarios" VALUES (19, '777', 'PEDRO HENRIQUE COSTA');
INSERT INTO public."TabUsuarios" VALUES (24, '7854', 'CLEIDE DE SOUZA');
INSERT INTO public."TabUsuarios" VALUES (29, '93939', 'GABRIELA COSTA');
INSERT INTO public."TabUsuarios" VALUES (26, '555', 'MANE GARRINCHA');
INSERT INTO public."TabUsuarios" VALUES (31, '6574', 'MARCIA DO CEU');
INSERT INTO public."TabUsuarios" VALUES (4, '3', 'TERESA SILVA');
INSERT INTO public."TabUsuarios" VALUES (32, '554', 'MARCIO NARIGAO');
INSERT INTO public."TabUsuarios" VALUES (20, '78787', 'TÃO - GILBERTO...');
INSERT INTO public."TabUsuarios" VALUES (25, '2424', 'ALEX RESMUNGÃOD');
INSERT INTO public."TabUsuarios" VALUES (28, '3434', 'JUNINHO VÓ OLGA');
INSERT INTO public."TabUsuarios" VALUES (30, '7785', 'FELIPE NIERIS');
INSERT INTO public."TabUsuarios" VALUES (6, '4', 'VALENTINA CAMARGO');
INSERT INTO public."TabUsuarios" VALUES (35, '66543', 'TUCO');
INSERT INTO public."TabUsuarios" VALUES (34, '553322', 'JULIA PIZARDO');
INSERT INTO public."TabUsuarios" VALUES (36, '77uu', 'XANDE');
INSERT INTO public."TabUsuarios" VALUES (37, '20', 'KID BENGALA PASSOU AQUI');
INSERT INTO public."TabUsuarios" VALUES (33, '477588', 'ELIANA DIAS PEREIRA ');
INSERT INTO public."TabUsuarios" VALUES (39, '123456789', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOXSSSSSSSSS');
INSERT INTO public."TabUsuarios" VALUES (40, '0987654321', 'ANDRE DA SILVA CAMARGO CORREIAAAAAAAAAAAAAAAAAAAAAAAAA....');


--
-- TOC entry 4530 (class 0 OID 19203)
-- Dependencies: 239
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: bdteste_496k_user
--



--
-- TOC entry 4532 (class 0 OID 19211)
-- Dependencies: 241
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: bdteste_496k_user
--



--
-- TOC entry 4543 (class 0 OID 0)
-- Dependencies: 236
-- Name: TabUsuarios_idUsuario_seq; Type: SEQUENCE SET; Schema: public; Owner: bdteste_496k_user
--

SELECT pg_catalog.setval('public."TabUsuarios_idUsuario_seq"', 40, true);


--
-- TOC entry 4544 (class 0 OID 0)
-- Dependencies: 238
-- Name: funcionario__id_seq; Type: SEQUENCE SET; Schema: public; Owner: bdteste_496k_user
--

SELECT pg_catalog.setval('public.funcionario__id_seq', 1, false);


--
-- TOC entry 4545 (class 0 OID 0)
-- Dependencies: 240
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bdteste_496k_user
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 1, false);


--
-- TOC entry 4394 (class 2606 OID 19200)
-- Name: TabUsuarios TabUsuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: bdteste_496k_user
--

ALTER TABLE ONLY public."TabUsuarios"
    ADD CONSTRAINT "TabUsuarios_pkey" PRIMARY KEY ("idUsuario");


--
-- TOC entry 4396 (class 2606 OID 19208)
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: bdteste_496k_user
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (_id);


--
-- TOC entry 4398 (class 2606 OID 19216)
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: bdteste_496k_user
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- TOC entry 4539 (class 0 OID 0)
-- Dependencies: 35
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: bdteste_496k_user
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2024-10-30 08:27:18

--
-- PostgreSQL database dump complete
--

