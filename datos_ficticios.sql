--
-- PostgreSQL database dump
--

\restrict WrtIYdUWFzeRoc5ZFgLbCXxnEEwzHodbkcdZFd3MdwiaoxhobVE2U7vdCOxvMw2

-- Dumped from database version 16.13
-- Dumped by pg_dump version 16.13

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
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.django_content_type VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type VALUES (2, 'auth', 'group');
INSERT INTO public.django_content_type VALUES (3, 'auth', 'permission');
INSERT INTO public.django_content_type VALUES (4, 'auth', 'user');
INSERT INTO public.django_content_type VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type VALUES (6, 'sessions', 'session');
INSERT INTO public.django_content_type VALUES (7, 'proveedores', 'proveedor');
INSERT INTO public.django_content_type VALUES (8, 'facturas', 'factura');
INSERT INTO public.django_content_type VALUES (9, 'pagos', 'archivopagos');
INSERT INTO public.django_content_type VALUES (10, 'pagos', 'registropago');
INSERT INTO public.django_content_type VALUES (11, 'conciliacion', 'coincidencia');
INSERT INTO public.django_content_type VALUES (12, 'conciliacion', 'procesoreconciliacion');
INSERT INTO public.django_content_type VALUES (13, 'certificados', 'certificadobancario');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.auth_permission VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission VALUES (5, 'Can add permission', 3, 'add_permission');
INSERT INTO public.auth_permission VALUES (6, 'Can change permission', 3, 'change_permission');
INSERT INTO public.auth_permission VALUES (7, 'Can delete permission', 3, 'delete_permission');
INSERT INTO public.auth_permission VALUES (8, 'Can view permission', 3, 'view_permission');
INSERT INTO public.auth_permission VALUES (9, 'Can add group', 2, 'add_group');
INSERT INTO public.auth_permission VALUES (10, 'Can change group', 2, 'change_group');
INSERT INTO public.auth_permission VALUES (11, 'Can delete group', 2, 'delete_group');
INSERT INTO public.auth_permission VALUES (12, 'Can view group', 2, 'view_group');
INSERT INTO public.auth_permission VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO public.auth_permission VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO public.auth_permission VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO public.auth_permission VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO public.auth_permission VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO public.auth_permission VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO public.auth_permission VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO public.auth_permission VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO public.auth_permission VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO public.auth_permission VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO public.auth_permission VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO public.auth_permission VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO public.auth_permission VALUES (25, 'Can add proveedor', 7, 'add_proveedor');
INSERT INTO public.auth_permission VALUES (26, 'Can change proveedor', 7, 'change_proveedor');
INSERT INTO public.auth_permission VALUES (27, 'Can delete proveedor', 7, 'delete_proveedor');
INSERT INTO public.auth_permission VALUES (28, 'Can view proveedor', 7, 'view_proveedor');
INSERT INTO public.auth_permission VALUES (29, 'Can add factura', 8, 'add_factura');
INSERT INTO public.auth_permission VALUES (30, 'Can change factura', 8, 'change_factura');
INSERT INTO public.auth_permission VALUES (31, 'Can delete factura', 8, 'delete_factura');
INSERT INTO public.auth_permission VALUES (32, 'Can view factura', 8, 'view_factura');
INSERT INTO public.auth_permission VALUES (33, 'Can add archivo pagos', 9, 'add_archivopagos');
INSERT INTO public.auth_permission VALUES (34, 'Can change archivo pagos', 9, 'change_archivopagos');
INSERT INTO public.auth_permission VALUES (35, 'Can delete archivo pagos', 9, 'delete_archivopagos');
INSERT INTO public.auth_permission VALUES (36, 'Can view archivo pagos', 9, 'view_archivopagos');
INSERT INTO public.auth_permission VALUES (37, 'Can add registro pago', 10, 'add_registropago');
INSERT INTO public.auth_permission VALUES (38, 'Can change registro pago', 10, 'change_registropago');
INSERT INTO public.auth_permission VALUES (39, 'Can delete registro pago', 10, 'delete_registropago');
INSERT INTO public.auth_permission VALUES (40, 'Can view registro pago', 10, 'view_registropago');
INSERT INTO public.auth_permission VALUES (41, 'Can add proceso reconciliacion', 12, 'add_procesoreconciliacion');
INSERT INTO public.auth_permission VALUES (42, 'Can change proceso reconciliacion', 12, 'change_procesoreconciliacion');
INSERT INTO public.auth_permission VALUES (43, 'Can delete proceso reconciliacion', 12, 'delete_procesoreconciliacion');
INSERT INTO public.auth_permission VALUES (44, 'Can view proceso reconciliacion', 12, 'view_procesoreconciliacion');
INSERT INTO public.auth_permission VALUES (45, 'Can add coincidencia', 11, 'add_coincidencia');
INSERT INTO public.auth_permission VALUES (46, 'Can change coincidencia', 11, 'change_coincidencia');
INSERT INTO public.auth_permission VALUES (47, 'Can delete coincidencia', 11, 'delete_coincidencia');
INSERT INTO public.auth_permission VALUES (48, 'Can view coincidencia', 11, 'view_coincidencia');
INSERT INTO public.auth_permission VALUES (49, 'Can add certificado bancario', 13, 'add_certificadobancario');
INSERT INTO public.auth_permission VALUES (50, 'Can change certificado bancario', 13, 'change_certificadobancario');
INSERT INTO public.auth_permission VALUES (51, 'Can delete certificado bancario', 13, 'delete_certificadobancario');
INSERT INTO public.auth_permission VALUES (52, 'Can view certificado bancario', 13, 'view_certificadobancario');


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.auth_user VALUES (2, 'pbkdf2_sha256$1200000$lAKp6iyhrcjlmrDsOzyxpS$+OJYXGh845wWbvaw0Q0/O+1FV+uEBr7hP+LMYvAbl4c=', '2026-03-24 20:04:02.995343+00', false, 'usuario', '', '', 'usuario@veripay.com', false, true, '2026-03-24 20:03:03.50556+00');
INSERT INTO public.auth_user VALUES (1, 'pbkdf2_sha256$1200000$lMhhIxpvpGTU24ezvUzFIp$HsoGk94LzH3J4mUepmuEzgvQvenYXzqhG0H9OMDNtcw=', '2026-03-24 20:07:41.371738+00', true, 'admin', '', '', 'admin@veripay.com', true, true, '2026-03-24 20:03:03.340227+00');


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: certificados_certificadobancario; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.certificados_certificadobancario VALUES ('93310595-a76c-4e72-9adb-7e9f09cafa53', 'CERT-001', 'Bancolombia', '0012345678', 1500000.00, '2026-03-22', 'FAC-001', true, '2026-03-24 20:03:04.885218+00');
INSERT INTO public.certificados_certificadobancario VALUES ('377f463d-01d4-4601-8b4f-2d62b12ffaa0', 'CERT-002', 'Bancolombia', '0012345678', 2300000.00, '2026-03-22', 'FAC-002', true, '2026-03-24 20:03:04.887538+00');
INSERT INTO public.certificados_certificadobancario VALUES ('f40c7f03-1416-4fa4-b7a3-fc2ee730ff4b', 'CERT-003', 'Davivienda', '0098765432', 800000.00, '2026-03-22', 'FAC-003', true, '2026-03-24 20:03:04.889517+00');
INSERT INTO public.certificados_certificadobancario VALUES ('19a27dcd-f925-4f1c-80a1-ef9d36420f06', 'CERT-004', 'BBVA', '0055667788', 3200000.00, '2026-03-22', 'FAC-005', false, '2026-03-24 20:03:04.891193+00');
INSERT INTO public.certificados_certificadobancario VALUES ('ff341e24-369a-4171-aca7-fa62165888d8', 'CERT-005', 'Banco de Bogotá', '0011223344', 5600000.00, '2026-03-22', 'FAC-007', true, '2026-03-24 20:03:04.892792+00');
INSERT INTO public.certificados_certificadobancario VALUES ('496fed5d-fa7c-472c-93ba-74b581426321', 'CERT-006', 'Bancolombia', '0012345678', 4100000.00, '2026-03-22', 'FAC-011', true, '2026-03-24 20:03:04.89434+00');
INSERT INTO public.certificados_certificadobancario VALUES ('d61e4ee1-0dc5-469a-9668-428b32657290', 'CERT-007', 'Davivienda', '0098765432', 3400000.00, '2026-03-22', 'FAC-014', false, '2026-03-24 20:03:04.895888+00');


--
-- Data for Name: conciliacion_procesoreconciliacion; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: proveedores_proveedor; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.proveedores_proveedor VALUES ('745f6270-7f49-4ee5-a6e5-a8b485f6740b', 'Distribuciones ABC S.A.S', '900123456-1', 'contacto@abc.com', '3001234567', '2026-03-24 20:03:04.804486+00', '2026-03-24 20:03:04.804497+00');
INSERT INTO public.proveedores_proveedor VALUES ('1811db65-89dc-4d88-a560-d6d8748cb4f7', 'Suministros XYZ Ltda', '800987654-2', 'ventas@xyz.com', '3109876543', '2026-03-24 20:03:04.807625+00', '2026-03-24 20:03:04.807632+00');
INSERT INTO public.proveedores_proveedor VALUES ('ba7788e5-51d5-429e-bee5-65a9356fe850', 'Importaciones del Valle', '901555666-3', 'info@impvalle.com', '3205556666', '2026-03-24 20:03:04.809688+00', '2026-03-24 20:03:04.809696+00');
INSERT INTO public.proveedores_proveedor VALUES ('347fc8ba-0984-4cfa-892d-83a0408da006', 'Tecnología Global S.A', '900777888-4', 'admin@tecglobal.com', '3107778888', '2026-03-24 20:03:04.811536+00', '2026-03-24 20:03:04.811544+00');
INSERT INTO public.proveedores_proveedor VALUES ('29d8a2bc-f8a1-4bdc-8433-53a329735fdf', 'Papelería El Lápiz', '800333444-5', 'pedidos@ellapiz.com', '3013334444', '2026-03-24 20:03:04.813471+00', '2026-03-24 20:03:04.813478+00');
INSERT INTO public.proveedores_proveedor VALUES ('498516ad-8c97-4e6b-901b-6215dbd42500', 'Ferretería Industrial Ltda', '901222333-6', 'ventas@ferreindustrial.com', '3152223333', '2026-03-24 20:03:04.815124+00', '2026-03-24 20:03:04.815132+00');
INSERT INTO public.proveedores_proveedor VALUES ('71f04051-82d2-4f56-a6f1-d559a2813eb9', 'Alimentos del Campo S.A.S', '900444555-7', 'pedidos@alicampo.com', '3204445555', '2026-03-24 20:03:04.816837+00', '2026-03-24 20:03:04.816845+00');
INSERT INTO public.proveedores_proveedor VALUES ('113c6973-0348-4f0a-b4c7-084ea0d5a08c', 'Servicios Logísticos Express', '800666777-8', 'operaciones@logexpress.com', '3016667777', '2026-03-24 20:03:04.818392+00', '2026-03-24 20:03:04.818399+00');


--
-- Data for Name: facturas_factura; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.facturas_factura VALUES ('07fe4809-48ab-4fb9-b6a7-ef7f0210d288', 'FAC-001', NULL, 1500000.00, 0.00, '2026-02-22', '2026-03-24', 'PENDIENTE', '2026-03-24 20:03:04.820987+00', '2026-03-24 20:03:04.820993+00', '745f6270-7f49-4ee5-a6e5-a8b485f6740b');
INSERT INTO public.facturas_factura VALUES ('cd9ff15c-1a59-4886-a01c-dc929606b369', 'FAC-002', NULL, 2300000.00, 0.00, '2026-02-24', '2026-03-26', 'PENDIENTE', '2026-03-24 20:03:04.824131+00', '2026-03-24 20:03:04.824138+00', '745f6270-7f49-4ee5-a6e5-a8b485f6740b');
INSERT INTO public.facturas_factura VALUES ('34ad3a04-df1a-42ac-897d-bdfb5e0aa1dc', 'FAC-003', NULL, 800000.00, 0.00, '2026-02-26', '2026-03-28', 'PENDIENTE', '2026-03-24 20:03:04.826934+00', '2026-03-24 20:03:04.82694+00', '1811db65-89dc-4d88-a560-d6d8748cb4f7');
INSERT INTO public.facturas_factura VALUES ('13e51872-d134-4442-9976-6f2bed26a237', 'FAC-004', NULL, 450000.00, 0.00, '2026-02-28', '2026-03-30', 'PENDIENTE', '2026-03-24 20:03:04.82888+00', '2026-03-24 20:03:04.828885+00', '1811db65-89dc-4d88-a560-d6d8748cb4f7');
INSERT INTO public.facturas_factura VALUES ('d17622ea-3f67-4976-ac1f-dda83d9416ed', 'FAC-005', NULL, 3200000.00, 0.00, '2026-03-02', '2026-04-01', 'PENDIENTE', '2026-03-24 20:03:04.830762+00', '2026-03-24 20:03:04.830767+00', 'ba7788e5-51d5-429e-bee5-65a9356fe850');
INSERT INTO public.facturas_factura VALUES ('3b32a002-6539-4daa-baaf-c77315fab49e', 'FAC-006', NULL, 1100000.00, 0.00, '2026-03-04', '2026-04-03', 'PENDIENTE', '2026-03-24 20:03:04.832598+00', '2026-03-24 20:03:04.832603+00', 'ba7788e5-51d5-429e-bee5-65a9356fe850');
INSERT INTO public.facturas_factura VALUES ('be7aa7bf-28da-4946-9953-e7fdc5a7ff55', 'FAC-007', NULL, 5600000.00, 0.00, '2026-03-06', '2026-04-05', 'PENDIENTE', '2026-03-24 20:03:04.834258+00', '2026-03-24 20:03:04.834262+00', '347fc8ba-0984-4cfa-892d-83a0408da006');
INSERT INTO public.facturas_factura VALUES ('4d9e63d8-aa2e-4269-b4a9-8f359e3ed23f', 'FAC-008', NULL, 780000.00, 0.00, '2026-03-08', '2026-04-07', 'PENDIENTE', '2026-03-24 20:03:04.836751+00', '2026-03-24 20:03:04.836757+00', '347fc8ba-0984-4cfa-892d-83a0408da006');
INSERT INTO public.facturas_factura VALUES ('3e435aeb-7cf2-4f3b-ae5f-9de9c4dddbe3', 'FAC-009', NULL, 250000.00, 0.00, '2026-03-10', '2026-04-09', 'PENDIENTE', '2026-03-24 20:03:04.839222+00', '2026-03-24 20:03:04.839228+00', '29d8a2bc-f8a1-4bdc-8433-53a329735fdf');
INSERT INTO public.facturas_factura VALUES ('759f816e-963b-4bec-bd1d-c1b597e9338f', 'FAC-010', NULL, 620000.00, 0.00, '2026-03-12', '2026-04-11', 'PENDIENTE', '2026-03-24 20:03:04.841568+00', '2026-03-24 20:03:04.841575+00', '29d8a2bc-f8a1-4bdc-8433-53a329735fdf');
INSERT INTO public.facturas_factura VALUES ('6c0e5b7d-18a2-405e-86db-217e1ce02269', 'FAC-011', NULL, 4100000.00, 0.00, '2026-03-14', '2026-04-13', 'PENDIENTE', '2026-03-24 20:03:04.844054+00', '2026-03-24 20:03:04.84406+00', '498516ad-8c97-4e6b-901b-6215dbd42500');
INSERT INTO public.facturas_factura VALUES ('f1a016b6-92c5-49f8-b8ef-000560eb5264', 'FAC-012', NULL, 980000.00, 0.00, '2026-03-16', '2026-04-15', 'PENDIENTE', '2026-03-24 20:03:04.846722+00', '2026-03-24 20:03:04.846732+00', '71f04051-82d2-4f56-a6f1-d559a2813eb9');
INSERT INTO public.facturas_factura VALUES ('ee4e3d31-8664-494a-9f27-54c07ebc530f', 'FAC-013', NULL, 1750000.00, 0.00, '2026-03-18', '2026-04-17', 'PENDIENTE', '2026-03-24 20:03:04.849141+00', '2026-03-24 20:03:04.849147+00', '71f04051-82d2-4f56-a6f1-d559a2813eb9');
INSERT INTO public.facturas_factura VALUES ('a6b8f6de-50fc-47a7-9b05-b19150978486', 'FAC-014', NULL, 3400000.00, 0.00, '2026-03-20', '2026-04-19', 'PENDIENTE', '2026-03-24 20:03:04.851931+00', '2026-03-24 20:03:04.851936+00', '113c6973-0348-4f0a-b4c7-084ea0d5a08c');
INSERT INTO public.facturas_factura VALUES ('d727ac88-302b-403c-85d6-fd8dc6fdede6', 'FAC-015', NULL, 560000.00, 0.00, '2026-03-22', '2026-04-21', 'PENDIENTE', '2026-03-24 20:03:04.854204+00', '2026-03-24 20:03:04.854209+00', '113c6973-0348-4f0a-b4c7-084ea0d5a08c');


--
-- Data for Name: pagos_archivopagos; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.pagos_archivopagos VALUES ('6d292985-983b-4206-b905-bcd8dd2b363a', '', 'csv', 10, 10, true, '2026-03-24 20:03:04.855568+00', '2026-03-24 20:03:04.85682+00');


--
-- Data for Name: pagos_registropago; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.pagos_registropago VALUES ('bcbb7de4-dd80-4ab3-818e-006d5da1c320', 'FAC-001', 1500000.00, '2026-03-19', 'Pago factura FAC-001', 0, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('7e4be6d6-89ab-4b78-bec6-539a0108b482', 'FAC-002', 2300000.00, '2026-03-19', 'Pago factura FAC-002', 1, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('0c04bf94-a718-4f07-8c24-51f8514704e1', 'FAC-003', 800000.00, '2026-03-21', 'Pago factura FAC-003', 2, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('6b2da143-4681-4bfc-8c1d-15f164cbc741', 'FAC-004', 200000.00, '2026-03-21', 'Pago parcial FAC-004', 3, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('0997f6d3-bdad-458b-b0e3-2265d346a2e4', 'FAC-005', 3200000.00, '2026-03-22', 'Pago factura FAC-005', 4, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('6b327dfd-7644-4d87-a845-eccedbd57094', 'FAC-007', 5600000.00, '2026-03-23', 'Pago factura FAC-007', 5, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('ba2f0765-2694-4e1f-9e26-d80c43078a5a', 'FAC-009', 250000.00, '2026-03-23', 'Pago factura FAC-009', 6, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('a015b44e-983b-4cf7-a5f6-62c03d59a0a5', 'FAC-011', 4100000.00, '2026-03-24', 'Pago factura FAC-011', 7, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('456f6ced-b0a7-4bcf-a11d-f964d03ca3e3', 'FAC-012', 980000.00, '2026-03-24', 'Pago factura FAC-012', 8, '6d292985-983b-4206-b905-bcd8dd2b363a');
INSERT INTO public.pagos_registropago VALUES ('9aee4783-a437-4070-8818-e97215dab5b9', 'FAC-014', 3400000.00, '2026-03-24', 'Pago factura FAC-014', 9, '6d292985-983b-4206-b905-bcd8dd2b363a');


--
-- Data for Name: conciliacion_coincidencia; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: veripay_user
--



--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.django_migrations VALUES (1, 'contenttypes', '0001_initial', '2026-03-24 20:03:01.36339+00');
INSERT INTO public.django_migrations VALUES (2, 'auth', '0001_initial', '2026-03-24 20:03:01.429099+00');
INSERT INTO public.django_migrations VALUES (3, 'admin', '0001_initial', '2026-03-24 20:03:01.446896+00');
INSERT INTO public.django_migrations VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2026-03-24 20:03:01.451638+00');
INSERT INTO public.django_migrations VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2026-03-24 20:03:01.456654+00');
INSERT INTO public.django_migrations VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2026-03-24 20:03:01.467051+00');
INSERT INTO public.django_migrations VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2026-03-24 20:03:01.47292+00');
INSERT INTO public.django_migrations VALUES (8, 'auth', '0003_alter_user_email_max_length', '2026-03-24 20:03:01.478587+00');
INSERT INTO public.django_migrations VALUES (9, 'auth', '0004_alter_user_username_opts', '2026-03-24 20:03:01.484541+00');
INSERT INTO public.django_migrations VALUES (10, 'auth', '0005_alter_user_last_login_null', '2026-03-24 20:03:01.490108+00');
INSERT INTO public.django_migrations VALUES (11, 'auth', '0006_require_contenttypes_0002', '2026-03-24 20:03:01.491986+00');
INSERT INTO public.django_migrations VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2026-03-24 20:03:01.496776+00');
INSERT INTO public.django_migrations VALUES (13, 'auth', '0008_alter_user_username_max_length', '2026-03-24 20:03:01.509029+00');
INSERT INTO public.django_migrations VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2026-03-24 20:03:01.515488+00');
INSERT INTO public.django_migrations VALUES (15, 'auth', '0010_alter_group_name_max_length', '2026-03-24 20:03:01.522521+00');
INSERT INTO public.django_migrations VALUES (16, 'auth', '0011_update_proxy_permissions', '2026-03-24 20:03:01.527854+00');
INSERT INTO public.django_migrations VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2026-03-24 20:03:01.534241+00');
INSERT INTO public.django_migrations VALUES (18, 'certificados', '0001_initial', '2026-03-24 20:03:01.544482+00');
INSERT INTO public.django_migrations VALUES (19, 'pagos', '0001_initial', '2026-03-24 20:03:01.54848+00');
INSERT INTO public.django_migrations VALUES (20, 'pagos', '0002_registropago', '2026-03-24 20:03:01.557152+00');
INSERT INTO public.django_migrations VALUES (21, 'proveedores', '0001_initial', '2026-03-24 20:03:01.568719+00');
INSERT INTO public.django_migrations VALUES (22, 'facturas', '0001_initial', '2026-03-24 20:03:01.581191+00');
INSERT INTO public.django_migrations VALUES (23, 'conciliacion', '0001_initial', '2026-03-24 20:03:01.586615+00');
INSERT INTO public.django_migrations VALUES (24, 'conciliacion', '0002_coincidencia', '2026-03-24 20:03:01.608152+00');
INSERT INTO public.django_migrations VALUES (25, 'sessions', '0001_initial', '2026-03-24 20:03:01.619152+00');


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: veripay_user
--

INSERT INTO public.django_session VALUES ('h8686onrwxwy23grz6g8uzyol3eyuahd', '.eJxVjDsOwjAQBe_iGln-O6ak5wzW7nqDA8iR4qRC3B0ipYD2zcx7iQzbWvPWeclTEWehxel3Q6AHtx2UO7TbLGlu6zKh3BV50C6vc-Hn5XD_Dir0-q2JvRljiiVY5IFCAA2lsPKYwCurmbxGsENAF5HM6EwgBSmm5I1zlsX7A_vNOAM:1w582P:Bg8vWrURAEO1WlsVjg651cBBK9wFDhvWQbrPLMTQ96Q', '2026-04-07 20:07:41.374346+00');


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: veripay_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 25, true);


--
-- PostgreSQL database dump complete
--

\unrestrict WrtIYdUWFzeRoc5ZFgLbCXxnEEwzHodbkcdZFd3MdwiaoxhobVE2U7vdCOxvMw2

