-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 21, 2025 at 03:57 PM
-- Server version: 8.0.36
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `physiotherapy_home_assistant`
--

-- --------------------------------------------------------

--
-- Table structure for table `authority_admin_list`
--

CREATE TABLE `authority_admin_list` (
  `id` bigint NOT NULL,
  `fname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `lname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `category` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gender` varchar(6) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `authority_admin_list`
--

INSERT INTO `authority_admin_list` (`id`, `fname`, `lname`, `email`, `phone`, `password`, `category`, `image`, `gender`) VALUES
(1, 'Tawhid', 'Mostafa', 'tawhid@gmail.com', '01770150230', '654987', 'full', '/media/Admin/360_F_477298099_GSuauTPwx8sj5j0gV5X9Qslbrmka9lDI.jpg', 'male'),
(4, 'Jannatun', 'naeem raisa', 'jannatun@gmail.com', '01234569877', '1234', 'mid', '', 'female');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add active_patient_list', 7, 'add_active_patient_list'),
(26, 'Can change active_patient_list', 7, 'change_active_patient_list'),
(27, 'Can delete active_patient_list', 7, 'delete_active_patient_list'),
(28, 'Can view active_patient_list', 7, 'view_active_patient_list'),
(29, 'Can add disease_category', 8, 'add_disease_category'),
(30, 'Can change disease_category', 8, 'change_disease_category'),
(31, 'Can delete disease_category', 8, 'delete_disease_category'),
(32, 'Can view disease_category', 8, 'view_disease_category'),
(33, 'Can add patient_list', 9, 'add_patient_list'),
(34, 'Can change patient_list', 9, 'change_patient_list'),
(35, 'Can delete patient_list', 9, 'delete_patient_list'),
(36, 'Can view patient_list', 9, 'view_patient_list'),
(37, 'Can add patient_list_temp', 10, 'add_patient_list_temp'),
(38, 'Can change patient_list_temp', 10, 'change_patient_list_temp'),
(39, 'Can delete patient_list_temp', 10, 'delete_patient_list_temp'),
(40, 'Can view patient_list_temp', 10, 'view_patient_list_temp'),
(41, 'Can add doctor_list', 11, 'add_doctor_list'),
(42, 'Can change doctor_list', 11, 'change_doctor_list'),
(43, 'Can delete doctor_list', 11, 'delete_doctor_list'),
(44, 'Can view doctor_list', 11, 'view_doctor_list'),
(45, 'Can add doctor_list_temp', 12, 'add_doctor_list_temp'),
(46, 'Can change doctor_list_temp', 12, 'change_doctor_list_temp'),
(47, 'Can delete doctor_list_temp', 12, 'delete_doctor_list_temp'),
(48, 'Can view doctor_list_temp', 12, 'view_doctor_list_temp'),
(49, 'Can add doctor_patient_list', 13, 'add_doctor_patient_list'),
(50, 'Can change doctor_patient_list', 13, 'change_doctor_patient_list'),
(51, 'Can delete doctor_patient_list', 13, 'delete_doctor_patient_list'),
(52, 'Can view doctor_patient_list', 13, 'view_doctor_patient_list'),
(53, 'Can add doctor deactive', 14, 'add_doctordeactive'),
(54, 'Can change doctor deactive', 14, 'change_doctordeactive'),
(55, 'Can delete doctor deactive', 14, 'delete_doctordeactive'),
(56, 'Can view doctor deactive', 14, 'view_doctordeactive'),
(57, 'Can add exercise_list', 15, 'add_exercise_list'),
(58, 'Can change exercise_list', 15, 'change_exercise_list'),
(59, 'Can delete exercise_list', 15, 'delete_exercise_list'),
(60, 'Can view exercise_list', 15, 'view_exercise_list'),
(61, 'Can add admin_list', 16, 'add_admin_list'),
(62, 'Can change admin_list', 16, 'change_admin_list'),
(63, 'Can delete admin_list', 16, 'delete_admin_list'),
(64, 'Can view admin_list', 16, 'view_admin_list'),
(65, 'Can add note exercise2', 17, 'add_noteexercise2'),
(66, 'Can change note exercise2', 17, 'change_noteexercise2'),
(67, 'Can delete note exercise2', 17, 'delete_noteexercise2'),
(68, 'Can view note exercise2', 17, 'view_noteexercise2'),
(69, 'Can add notificationes2', 18, 'add_notificationes2'),
(70, 'Can change notificationes2', 18, 'change_notificationes2'),
(71, 'Can delete notificationes2', 18, 'delete_notificationes2'),
(72, 'Can view notificationes2', 18, 'view_notificationes2'),
(73, 'Can add result ex', 19, 'add_resultex'),
(74, 'Can change result ex', 19, 'change_resultex'),
(75, 'Can delete result ex', 19, 'delete_resultex'),
(76, 'Can view result ex', 19, 'view_resultex'),
(77, 'Can add notification', 20, 'add_notification'),
(78, 'Can change notification', 20, 'change_notification'),
(79, 'Can delete notification', 20, 'delete_notification'),
(80, 'Can view notification', 20, 'view_notification');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(16, 'authority', 'admin_list'),
(5, 'contenttypes', 'contenttype'),
(14, 'doctor', 'doctordeactive'),
(11, 'doctor', 'doctor_list'),
(12, 'doctor', 'doctor_list_temp'),
(13, 'doctor', 'doctor_patient_list'),
(15, 'doctor', 'exercise_list'),
(7, 'patient', 'active_patient_list'),
(8, 'patient', 'disease_category'),
(9, 'patient', 'patient_list'),
(10, 'patient', 'patient_list_temp'),
(6, 'sessions', 'session'),
(17, 'temp', 'noteexercise2'),
(20, 'temp', 'notification'),
(18, 'temp', 'notificationes2'),
(19, 'temp', 'resultex');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-19 16:10:13.151530'),
(2, 'auth', '0001_initial', '2024-05-19 16:10:13.683589'),
(3, 'admin', '0001_initial', '2024-05-19 16:10:13.819776'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-19 16:10:13.826002'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-19 16:10:13.829980'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-19 16:10:13.929480'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-19 16:10:13.996855'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-19 16:10:14.038608'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-19 16:10:14.044655'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-19 16:10:14.106970'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-19 16:10:14.109879'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-19 16:10:14.113896'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-19 16:10:14.188427'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-19 16:10:14.259472'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-19 16:10:14.292022'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-19 16:10:14.298030'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-19 16:10:14.369463'),
(18, 'authority', '0001_initial', '2024-05-19 16:10:14.406685'),
(19, 'authority', '0002_admin_list_gender', '2024-05-19 16:10:14.423235'),
(20, 'authority', '0003_alter_admin_list_image', '2024-05-19 16:10:14.426572'),
(21, 'doctor', '0001_initial', '2024-05-19 16:10:14.533528'),
(22, 'patient', '0001_initial', '2024-05-19 16:10:14.633673'),
(23, 'sessions', '0001_initial', '2024-05-19 16:10:14.669726'),
(24, 'temp', '0001_initial', '2024-05-19 16:10:14.787736'),
(25, 'doctor', '0002_doctor_patient_list_date', '2024-05-30 11:55:02.289316'),
(26, 'patient', '0002_active_patient_list_date_active_patient_list_pid', '2024-05-30 11:58:17.544096'),
(27, 'patient', '0003_alter_active_patient_list_pid', '2024-05-30 12:00:23.766802'),
(28, 'doctor', '0003_doctor_patient_list_aldid', '2024-05-30 15:49:51.038731');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('85p8u87ovjcjsbct8tmly6dxuay2qlxx', 'eyJvdHBfZXhwaXJ5IjoiMjAyNC0wOS0wOFQyMjowNjoxOS43NzAwNDUiLCJuYW1lIjoiVGF3aGlkIE1vc3RhZmEiLCJhZGVtYWlscyI6InRhd2hpZEBnbWFpbC5jb20ifQ:1snMuT:e7fKTaRfIaF3p3kHNIhP-XypdLIdc4CCRZ4MHubGQ-g', '2024-09-22 18:45:17.327426'),
('90plwuil6dwzvmdrjeq9tjhizgz8uy51', 'eyJhZGVtYWlscyI6InRhd2hpZEBnbWFpbC5jb20ifQ:1snKLt:flTi8Ly05gNcF3MaPU0QE2Qvko1lXECLjOPmVLaI8H4', '2024-09-22 16:01:25.405616'),
('a51h314hoeqcyizlnkt9jbo6isdgcrrb', '.eJyrVspLzE1VslJyLC4u0Qsoyk_TcynSM1XITUw0NVTISMzJyQfSGgEhmko6SkGeLkpW5hbmRsYmluYWxuYGhjpKiSmpuYmZOcVAI0oSyzMyUxzSQXy95PxcoA6EXGl2XmpOam5OqUN6aVpprqEhWEUtAJoXJ-Y:1sU6sh:5P95sBm9tKl7uJz_FBx59_LSkh3XO-TlYwW50stJvKc', '2024-07-31 15:47:51.119072'),
('a8608u5hq14v7ic8ppbdsg1vimhn4hcw', '.eJyrVsovKYhPrSjILKpUslIyMjAy0TWw1DWwCDE0tDI1tTI10bO0MDQ1NVbSUUrNTczMKQaqSsnPTU1LzDM2sHBIzs_JLyqt0kvOzwWqyEvMTQXKZ2ck5ilkJBYn5gHFElPg-koSyzMyUxzSQXywjloAckMnxg:1sqEf3:T3LEfq1QL2waIkeQXsXVEKOYrAfd1TOG3SAKtTB3S2U', '2024-09-30 16:33:13.162848'),
('avl75v8eb0r8kq4c0pr2jltl5catp7gm', '.eJyrVkpMSc1NzMwpVrJSKkksz8hMcUgH8fWS83OVdJQQkrn5RZlpiVlmpoYOKRWZyalQBXmJualAWcfi4vxkvYCi_DQ9lyI9hWyg4lyFxIzc1BQFjYAQTaVaAHKFIxM:1sTyfD:w2CKa1e4S5bPuWQuWAvdTkIHDkT_sAcHckD21ty6W1E', '2024-07-31 07:01:23.788753'),
('ch612wj98u1cbnn83w9phvvnl8g62ytg', 'eyJuYW1lIjoiVGF3aGlkIE1vc3RhZmEiLCJhZGVtYWlscyI6InRhd2hpZEBnbWFpbC5jb20ifQ:1sOXXK:pLr47QvCVhzcOWHXXhf9xzfRiZAjjS4riSOIaXG2j8Q', '2024-07-16 07:02:46.029325'),
('f1cajrbmnxbplq3tct7ir8af500c3wu6', 'eyJuYW1lIjoibWVnbGEga2FrdSIsImVtYWlscyI6InR1a25lbGVtbHVAZ3VmdW0xLmNvbSJ9:1s8kFG:Lf65D0E_h7piFuf7fPkaipfbHVUkJXej2JdbiWeQvlA', '2024-06-02 17:22:50.516117'),
('fbk0i3nfj7p4xocek78mi4twkut1uw2v', '.eJyrVkpMSc1NzMwpVrJSKkksz8hMcUgH8fWS83OVdJTySwqAEgZGlgZGJkAuSAauMDWltLg0CV15fGpFQWZRJVCVEVCProGprpFhiKGxlbG5lZGBnqm5gaWZOVBlXmJuKlBNCNgkBd_84pLEtESlWgD57ixk:1sCfDZ:qHQxJd-QJrd8N7KD1Zqj5ubSxtf2hfI76oMRpluQhys', '2024-06-13 12:49:17.898682'),
('gb32k4nw5tkdeo8ezkv8jvxhc66f2rv3', 'eyJlbWFpbHMiOiJkb21lZmFuMzA4QGNvbG9ydXouY29tIn0:1sogUj:oFcCdytuL--98-F_KyrbkZ3hFPMsTmck44oWVwJ62kY', '2024-09-26 09:52:09.981996'),
('gigo05za9ttqjgp72pwth5iibcyb4qd4', 'eyJuYW1lIjoia2hhbiBoYXNhbiIsImFkZW1haWxzIjoidGF3aGlkQGdtYWlsLmNvbSJ9:1t2nQk:Wx6mOpWMNxW22vfH6O2A8lQ5huEnuFV0PfeiKh2DFAI', '2024-11-04 08:06:22.099393'),
('rbbzbt9pirq6in4x92tmncb6nmfwe1ew', 'eyJuYW1lIjoia2hhbiBoYXNhbiJ9:1ttMjp:CNxwun2k8eXjyk5mtNOW7gWziPUOSLVdjV31TV5Bn-w', '2025-03-29 08:19:21.529353'),
('tgsxl39jig3tx0q73gfqxkyt060kfo36', 'eyJkZW1haWxzIjoibGFoaWp1YmUub3JhanVtZXZAam9sbHlmcmVlMS5jb20iLCJuYW1lIjoibWFhNTEifQ:1sDpEX:LF-F1Jb1_em9r6j6Rm_F0xR9EyhLEAxlGZRFaObN9wE', '2024-06-16 17:43:05.398495'),
('wdy6hpprj2f09fzeabfi876msnk7o402', 'eyJuYW1lIjoia2hhbiBoYXNhbiIsImFkZW1haWxzIjoidGF3aGlkQGdtYWlsLmNvbSJ9:1sqEgf:9LhmXAhhLZrVvmItNPjucMpyCpbefgUL-5KX3V5sbTs', '2024-09-30 16:34:53.671409'),
('yuo4o3xm006lv9u34eekvq238pc0gqq5', 'eyJhZGVtYWlscyI6InRhd2hpZEBnbWFpbC5jb20ifQ:1sZPTy:h9m9WMdvFMJ7BI-WyZSw0cKNdIP3zMjlW_8G8FdOn5o', '2024-08-15 06:40:14.507499');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_doctordeactive`
--

CREATE TABLE `doctor_doctordeactive` (
  `id` bigint NOT NULL,
  `DID` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_doctordeactive`
--

INSERT INTO `doctor_doctordeactive` (`id`, `DID`, `date`, `time`) VALUES
(3, '9861011', '2024-07-10', '15:44:19.647964');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_doctor_list`
--

CREATE TABLE `doctor_doctor_list` (
  `id` bigint NOT NULL,
  `S_number` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `ltitle` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
  `NIDP_number` varchar(18) COLLATE utf8mb4_general_ci NOT NULL,
  `BPA_number` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `ephone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `ch_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `division` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `district` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `active` varchar(4) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_doctor_list`
--

INSERT INTO `doctor_doctor_list` (`id`, `S_number`, `title`, `first_name`, `last_name`, `ltitle`, `gender`, `NIDP_number`, `BPA_number`, `phone`, `ephone`, `email`, `password`, `ch_name`, `division`, `district`, `address`, `image`, `active`) VALUES
(1, '1000001', 'Prof.Dr.', 'Jannatun', 'Naeem Raisa', '(PT)', 'female', '1324567895', '1235468', '01770153230', '01770153230', 'eakbajechele@gmail.com', '1234', 'AR Hospital', 'rajshahi', 'rajshahi', '4/4 road', '/media/doctor/FB_IMG_1650063498957.jpg', 'yes'),
(2, '1293561', 'Dr.', 'Hamid', 'Khan', '(PT)', 'male', '9876543211', '654321', '01234567891', '12365478999', 'gotosi1814@funvane.com', '123', 'Hallo Hospital', 'rajshahi', 'rajshahi', '40/4 road', '', 'yes'),
(3, '1405752', 'Assoc.Prof.Dr.', 'korim', 'ahmed', '(PT)', 'male', '9876543211', '69325874', '98765432114', '98653274101', 'morifaj651@dxice.com', '123', 'Hallo Hospital', 'mymensingh', 'Mymensingh', '101/5', '/media/doctor/man-png-30110.png', 'no'),
(4, '2761695', 'Asst.Prof.Dr.', 'muhib', 'ahmed', '(PT)', 'male', '8523697410', '15975382', '02587413697', '02587539514', 'lahijube.orajumev@jollyfree.com', '123', 'hamid hospital', 'sylhet', 'Sunamganj', '400/5 road', '/media/doctor/gettyimages-507273724-612x612.jpg', 'yes'),
(5, '9861037', 'Dr.', 'adity', 'khan', '(PT)', 'female', '8796542313', '2468913', '88899997774', '55556666664', 'tuknelemlu@gufum.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', '/media/doctor/04.jpg', 'no'),
(8, '2761697', 'Asst.Prof.Dr.5', 'maa51', 'hallo51', '(PT)', 'male5', '8523697415', '15975385', '02587413695', '02587539511', 'lahijube.orajumev@jollyfree1.com', '123', 'hamid hospital55', 'sylhetH', 'SunamganjH', '400/5 road5', '/media/doctor/aa.png', 'yes'),
(9, '9861011', 'Dr.', 'a', 'kaka', '(PT)', 'female', '8796542313', '2468913', '88899997777', '55556666664', 'tuknelemlu@gufum4.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', '/media/doctor/04.jpg', 'yes'),
(10, '5975350', 'Dr.', 'hasib', 'mulla', '(PT)', 'male', '22135465555555555', '56488888', '85295467153', '51543625625', 'ninan48344@esterace.com', '123', 'hallo physio', 'barisal', 'Bhola', '4455/445 road', '', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_doctor_list_temp`
--

CREATE TABLE `doctor_doctor_list_temp` (
  `id` bigint NOT NULL,
  `title` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `ltitle` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
  `NIDP_number` varchar(18) COLLATE utf8mb4_general_ci NOT NULL,
  `BPA_number` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `ephone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `ch_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `division` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `district` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_doctor_list_temp`
--

INSERT INTO `doctor_doctor_list_temp` (`id`, `title`, `first_name`, `last_name`, `ltitle`, `gender`, `NIDP_number`, `BPA_number`, `phone`, `ephone`, `email`, `password`, `ch_name`, `division`, `district`, `address`, `image`) VALUES
(3, 'Assoc.Prof.Dr.', 'korim', 'ahmed', '(PT)', 'male', '9876543211', '69325874', '98765432114', '98653274101', 'morifaj651@dxice.com', '123', 'Hallo Hospital', 'mymensingh', 'Mymensingh', '101/5', ''),
(4, 'Asst.Prof.Dr.', 'muhib', 'ahmed', '(PT)', 'male', '8523697410', '15975382', '02587413697', '02587539514', 'lahijube.orajumev@jollyfree.com', '123', 'hamid hospital', 'sylhet', 'Sunamganj', '400/5 road', ''),
(5, 'Dr.', 'adity', 'khan', '(PT)', 'female', '8796542313', '2468913', '88899997774', '55556666664', 'tuknelemlu@gufum.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', ''),
(6, 'Dr.', 'hamid', 'Khan', '(PT)', 'male', '9876543211', '654321', '01234567891', '01234567891', 'gotosi1814@funvane.com', '123', 'hallo hospital', 'rangpur', 'Nilphamari', '11/11 road', ''),
(7, 'Assoc.Prof.Dr.', 'korim', 'ahmed', '(PT)', 'male', '9876543211', '69325874', '98765432114', '98653274101', 'morifaj651@dxice.com', '123', 'Hallo Hospital', 'mymensingh', 'Mymensingh', '101/5', ''),
(8, 'Asst.Prof.Dr.', 'muhib', 'ahmed', '(PT)', 'male', '8523697410', '15975382', '02587413697', '02587539514', 'lahijube.orajumev@jollyfree.com', '123', 'hamid hospital', 'sylhet', 'Sunamganj', '400/5 road', ''),
(9, 'Dr.', 'adity', 'khan', '(PT)', 'female', '8796542313', '2468913', '88899997774', '55556666664', 'tuknelemlu@gufum.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', ''),
(10, 'Dr.', 'hamid', 'Khan', '(PT)', 'male', '9876543211', '654321', '01234567891', '01234567891', 'gotosi1814@funvane.com', '123', 'hallo hospital', 'rangpur', 'Nilphamari', '11/11 road', ''),
(11, 'Assoc.Prof.Dr.', 'korim', 'ahmed', '(PT)', 'male', '9876543211', '69325874', '98765432114', '98653274101', 'morifaj651@dxice.com', '123', 'Hallo Hospital', 'mymensingh', 'Mymensingh', '101/5', ''),
(12, 'Asst.Prof.Dr.', 'muhib', 'ahmed', '(PT)', 'male', '8523697410', '15975382', '02587413697', '02587539514', 'lahijube.orajumev@jollyfree.com', '123', 'hamid hospital', 'sylhet', 'Sunamganj', '400/5 road', ''),
(13, 'Dr.', 'adity', 'khan', '(PT)', 'female', '8796542313', '2468913', '88899997774', '55556666664', 'tuknelemlu@gufum.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', ''),
(14, 'Dr.', 'hamid', 'Khan', '(PT)', 'male', '9876543211', '654321', '01234567891', '01234567891', 'gotosi1814@funvane.com', '123', 'hallo hospital', 'rangpur', 'Nilphamari', '11/11 road', ''),
(15, 'Assoc.Prof.Dr.', 'korim', 'ahmed', '(PT)', 'male', '9876543211', '69325874', '98765432114', '98653274101', 'morifaj651@dxice.com', '123', 'Hallo Hospital', 'mymensingh', 'Mymensingh', '101/5', ''),
(16, 'Asst.Prof.Dr.', 'muhib', 'ahmed', '(PT)', 'male', '8523697410', '15975382', '02587413697', '02587539514', 'lahijube.orajumev@jollyfree.com', '123', 'hamid hospital', 'sylhet', 'Sunamganj', '400/5 road', ''),
(17, 'Dr.', 'adity', 'khan', '(PT)', 'female', '8796542313', '2468913', '88899997774', '55556666664', 'tuknelemlu@gufum.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', ''),
(18, 'Dr.', 'hamid', 'Khan', '(PT)', 'male', '9876543211', '654321', '01234567891', '01234567891', 'gotosi1814@funvane.com', '123', 'hallo hospital', 'rangpur', 'Nilphamari', '11/11 road', ''),
(19, 'Assoc.Prof.Dr.', 'korim', 'ahmed', '(PT)', 'male', '9876543211', '69325874', '98765432114', '98653274101', 'morifaj651@dxice.com', '123', 'Hallo Hospital', 'mymensingh', 'Mymensingh', '101/5', ''),
(20, 'Asst.Prof.Dr.', 'muhib', 'ahmed', '(PT)', 'male', '8523697410', '15975382', '02587413697', '02587539514', 'lahijube.orajumev@jollyfree.com', '123', 'hamid hospital', 'sylhet', 'Sunamganj', '400/5 road', ''),
(21, 'Dr.', 'adity', 'khan', '(PT)', 'female', '8796542313', '2468913', '88899997774', '55556666664', 'tuknelemlu@gufum.com', '123', 'islamic hospital', 'barisal', 'Bhola', '10001/1 kuril road', ''),
(22, 'Dr.', 'hasib', 'mulla', '(PT)', 'male', '22135465555555555', '56488888', '85295467153', '51543625625', 'ninan48344@esterace.com', '123', 'hallo physio', 'barisal', 'Bhola', '4455/445 road', '');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_doctor_patient_list`
--

CREATE TABLE `doctor_doctor_patient_list` (
  `id` bigint NOT NULL,
  `DID` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
  `RID` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `PName` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `PDisease` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `PAge` int NOT NULL,
  `PPhone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `PEmail` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `PExercise` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `PDcategory` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `Date` date DEFAULT NULL,
  `alDID` varchar(8) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_doctor_patient_list`
--

INSERT INTO `doctor_doctor_patient_list` (`id`, `DID`, `RID`, `PName`, `PDisease`, `PAge`, `PPhone`, `PEmail`, `PExercise`, `PDcategory`, `Date`, `alDID`) VALUES
(1, '2761697', '6556973175794', 'megla', 'joint pain', 20, '12365478889', 'tuknelemlu@gufum11.com', 'E03, E04, E06', 'P02', '2024-05-27', '1293561'),
(2, '2761697', '2981744854424', 'megla', 'hip pain', 20, '12365478889', 'tuknelemlu@gufum1.com', 'E07, E08, E09', 'P03', '2024-05-24', '1000001'),
(3, '2761697', '7872349783701', 'megla', 'back pain', 20, '12365478888', 'tuknelemlu@gufum.com', 'E03, E06', 'P02', '2024-07-17', NULL),
(4, '5975350', '1426488133359', 'khan', 'khee pain', 24, '98765432154', 'domefan308@coloruz.com', 'E07, E08, E09', 'P04', '2024-09-08', '2761697'),
(5, '5975350', '3406569683637', 'megla', 'back pain', 20, '12365478888', 'tuknelemlu@gufum.com', 'E03, E06, E09', 'P02', '2024-10-08', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `doctor_exercise_list`
--

CREATE TABLE `doctor_exercise_list` (
  `id` bigint NOT NULL,
  `EID` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `EName` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `video` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_exercise_list`
--

INSERT INTO `doctor_exercise_list` (`id`, `EID`, `EName`, `image`, `video`) VALUES
(1, 'E01', 'Abduction', '/media/Exercise/a01.jpg', '/media/Exercise/Video/Abduction%20.mp4'),
(2, 'E02', 'Adduction', '/media/Exercise/a02.jpg', '/media/Exercise/Video/Aduction.mp4'),
(3, 'E03', 'Lateral Rotation', '/media/Exercise/a03.png', '/media/Exercise/Video/Lateral%20Rotation.mp4'),
(4, 'E04', 'Medial Rotation', '/media/Exercise/a04.png', '/media/Exercise/Video/Medial%20Rotation.mp4'),
(5, 'E05', 'Circumduction', '/media/Exercise/a05.jpg', '/media/Exercise/Video/Circumduction.mp4'),
(6, 'E06', 'Wrist Extension', '/media/Exercise/06.png', '/media/Exercise/Video/Wrist%20Extension.mp4'),
(7, 'E07', 'Hip Joint Flexion', '/media/Exercise/07.jpeg', '/media/Exercise/Video/Hip%20Joint%20Flection.mp4'),
(8, 'E08', 'Both Leg Flexion', '/media/Exercise/08.jpg', '/media/Exercise/Video/Both%20Leg%20Flection.mp4'),
(9, 'E09', 'Back Extension', '/media/Exercise/a09.jpg', '/media/Exercise/Video/Back%20Extension.mp4');

-- --------------------------------------------------------

--
-- Table structure for table `patient_active_patient_list`
--

CREATE TABLE `patient_active_patient_list` (
  `id` bigint NOT NULL,
  `pemail` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `pphone` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `DID` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
  `RID` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `Date` date DEFAULT NULL,
  `PID` varchar(11) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_active_patient_list`
--

INSERT INTO `patient_active_patient_list` (`id`, `pemail`, `pphone`, `DID`, `RID`, `Date`, `PID`) VALUES
(1, 'tuknelemlu@gufum11.com', '12365478880', '2761697', '6556973175794', '2024-05-28', '1235444546'),
(2, 'tuknelemlu@gufum11.com', '12365478880', '2761697', '2981744854424', '2024-05-30', '1235444546'),
(3, 'domefan308@coloruz.com', '98765432154', '5975350', '1426488133359', '2024-09-08', '1456173256');

-- --------------------------------------------------------

--
-- Table structure for table `patient_disease_category`
--

CREATE TABLE `patient_disease_category` (
  `id` bigint NOT NULL,
  `DeID` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
  `DName` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `DImage` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_disease_category`
--

INSERT INTO `patient_disease_category` (`id`, `DeID`, `DName`, `DImage`) VALUES
(1, 'P01', 'Shoulder Problem', '/media/DCatagory/01.jpeg'),
(2, 'P02', 'Elbow problem', '/media/DCatagory/02.jpg'),
(4, 'P03', 'Hip Problem', '/media/DCatagory/03p.jpg'),
(5, 'P04', 'Knee Problem', '/media/DCatagory/04.jpg'),
(6, 'P05', 'Back Problem', '/media/DCatagory/05p.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `patient_patient_list`
--

CREATE TABLE `patient_patient_list` (
  `id` bigint NOT NULL,
  `P_number` varchar(11) COLLATE utf8mb4_general_ci NOT NULL,
  `fname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `lname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `username` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `contact` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `econtact` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_patient_list`
--

INSERT INTO `patient_patient_list` (`id`, `P_number`, `fname`, `lname`, `username`, `gender`, `email`, `contact`, `econtact`, `password`, `address`, `image`) VALUES
(1, '1000000002', 'Jannatun', 'Naeem Raisa', 'raisa', 'female', 'eakbajechele@gmail.com', '01770153230', '01770153230', '1234', 'Rajshahi,Rajshahi,4/15 road', '/media/patient/FB_IMG_1650063498957.jpg'),
(2, '1000000022', 'Hamid', 'Khan', 'hamid', 'male', 'gotosi1814@funvane.com', '12365478900', '12345678900', '123', 'Rajshahi,Bangladesh', '/media/patient/man-png-30110.png'),
(3, '1000000033', 'korim', 'Khan', 'korim', 'male', 'morifaj651@dxice.com', '12365478911', '12345678900', '123', 'Dhaka,Banglasesh', '/media/patient/aa.png'),
(4, '1000000042', 'adity', 'Khan', 'adity', 'female', 'lahijube.orajumev@jollyfree.com', '12365478944', '12345678944', '123', 'Dhaka,Banglasesh', '/media/patient/Cute-little-boy-play-water_1920x1200.jpg'),
(5, '1235444545', 'megla', 'akter', 'megla', 'female', 'tuknelemlu@gufum.com', '12365478888', '12345678888', '123', 'Dhaka,Banglasesh', '/media/patient/Computer-Graphics-Animation-Simulation_CS348C.jpg'),
(8, '1235444546', 'megla', 'kaku', 'megla21', 'maled', 'tuknelemlu@gufum11.com', '12365478880', '12345678888', '123', 'Dhaka,dhaka,15/c dhanmondi', '/media/patient/Computer-Graphics-Animation-Simulation_CS348C.jpg'),
(9, '1456173256', 'khan', 'hasan', 'khan', 'male', 'domefan308@coloruz.com', '98765432154', '89778987898', '123', 'dhaka, Shariatpur, 4876/4A ', '');

-- --------------------------------------------------------

--
-- Table structure for table `patient_patient_list_temp`
--

CREATE TABLE `patient_patient_list_temp` (
  `id` bigint NOT NULL,
  `fname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `lname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `username` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `contact` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `econtact` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(250) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_patient_list_temp`
--

INSERT INTO `patient_patient_list_temp` (`id`, `fname`, `lname`, `username`, `gender`, `email`, `contact`, `econtact`, `password`, `address`, `image`) VALUES
(9, 'megla', 'akter', 'megla', '', 'tuknelemlu@gufum.com', '12365478888', '12345678888', '123', 'Dhaka,Banglasesh', ''),
(10, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(11, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(12, 'adity', 'Khan', 'adity', '', 'lahijube.orajumev@jollyfree.com', '12365478944', '12345678944', '123', 'Dhaka,Banglasesh', ''),
(13, 'megla', 'akter', 'megla', '', 'tuknelemlu@gufum.com', '12365478888', '12345678888', '123', 'Dhaka,Banglasesh', ''),
(14, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(15, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(16, 'adity', 'Khan', 'adity', '', 'lahijube.orajumev@jollyfree.com', '12365478944', '12345678944', '123', 'Dhaka,Banglasesh', ''),
(17, 'megla', 'akter', 'megla', '', 'tuknelemlu@gufum.com', '12365478888', '12345678888', '123', 'Dhaka,Banglasesh', ''),
(18, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(19, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(20, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(21, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(22, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(23, 'megla', 'Khan', 'meglas', '', 'aa@dxice.com', '12365478800', '12345678888', '123', 'Rajshahi,Bangladesh', ''),
(24, 'Tawhid', 'Mostafa', 'aaa', '', 'tawhid@gmail.com', '01234567891', '01234567891', '111', '1111', ''),
(25, 'Tawhid', 'Mostafa', 'aaa', '', 'tawhid@gmail.com', '01234567891', '01234567891', '111', 'dhaka, Narayanganj, Rajshahi,Bangladesh', ''),
(26, 'a', 'a', 'aaaaa', 'male', 'tawhidedusub@gmail.com', '11', '11', '12', 'rangpur, Panchagarh, wseswee', ''),
(27, 'a', 'a', 'aaaaa', 'male', 'tawhidedusub@gmail.com', '11', '11', '12', 'rangpur, Panchagarh, wseswee', ''),
(28, 'khan', 'hasan', 'khan', 'male', 'domefan308@coloruz.com', '98765432154', '89778987898', '123', 'dhaka, Shariatpur, 4876/4A ', '');

-- --------------------------------------------------------

--
-- Table structure for table `temp_noteexercise2`
--

CREATE TABLE `temp_noteexercise2` (
  `id` bigint NOT NULL,
  `RID` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `DID` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `notification_type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_date` date NOT NULL,
  `created_time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `temp_noteexercise2`
--

INSERT INTO `temp_noteexercise2` (`id`, `RID`, `DID`, `message`, `notification_type`, `created_at`, `created_date`, `created_time`) VALUES
(1, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-02 21:45:26.000000', '2024-07-02', '21:45:26.000000'),
(2, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-02 21:45:26.000000', '2024-07-02', '21:45:26.000000'),
(3, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-03 21:45:26.000000', '2024-07-03', '21:45:26.000000'),
(4, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-03 21:45:26.000000', '2024-07-03', '21:45:26.000000'),
(5, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-04 21:45:26.000000', '2024-07-04', '21:45:26.000000'),
(6, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-04 21:45:26.000000', '2024-07-04', '21:45:26.000000'),
(7, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-05 21:45:26.000000', '2024-07-05', '21:45:26.000000'),
(8, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-05 21:45:26.000000', '2024-07-05', '21:45:26.000000'),
(9, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-06 21:45:26.000000', '2024-07-06', '21:45:26.000000'),
(10, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-06 21:45:26.000000', '2024-07-06', '21:45:26.000000'),
(11, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-07 21:45:26.000000', '2024-07-07', '21:45:26.000000'),
(12, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-07 21:45:26.000000', '2024-07-07', '21:45:26.000000'),
(13, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-08 21:45:26.000000', '2024-07-08', '21:45:26.000000'),
(14, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-08 21:45:26.000000', '2024-07-08', '21:45:26.000000'),
(15, '6556973175794', '2761697', 'Your patient megla has not completed his/her exercise today', 'Doctor Notification', '2024-07-09 21:45:26.000000', '2024-07-09', '21:45:26.000000'),
(16, '6556973175794', NULL, 'You have not done your exercise today', 'Alert', '2024-07-09 21:45:26.000000', '2024-07-09', '21:45:26.000000');

-- --------------------------------------------------------

--
-- Table structure for table `temp_notification`
--

CREATE TABLE `temp_notification` (
  `id` bigint NOT NULL,
  `message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `notification_type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `recipient_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `temp_notificationes2`
--

CREATE TABLE `temp_notificationes2` (
  `id` bigint NOT NULL,
  `RID` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `DID` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `notification_type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_date` date NOT NULL,
  `created_time` time(6) NOT NULL,
  `read` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `temp_notificationes2`
--

INSERT INTO `temp_notificationes2` (`id`, `RID`, `DID`, `message`, `notification_type`, `created_at`, `created_date`, `created_time`, `read`) VALUES
(1, '6556973175794', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 16:56:21.888553', '2024-05-29', '16:56:21.888553', 0),
(2, '2981744854424', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 16:56:21.891559', '2024-05-29', '16:56:21.891559', 0),
(3, '6556973175794', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 16:57:02.844249', '2024-05-29', '16:57:02.844249', 0),
(4, '2981744854424', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 16:57:02.847227', '2024-05-29', '16:57:02.847227', 0),
(5, '6556973175794', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 17:01:00.615772', '2024-05-29', '17:01:00.615772', 0),
(6, '2981744854424', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 17:01:00.620016', '2024-05-29', '17:01:00.620016', 0),
(7, '6556973175794', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 17:12:10.893270', '2024-05-29', '17:12:10.893270', 0),
(8, '2981744854424', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 17:12:10.895269', '2024-05-29', '17:12:10.895269', 0),
(9, '6556973175794', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 17:12:18.077166', '2024-05-29', '17:12:18.077166', 0),
(10, '2981744854424', NULL, 'Your exercise for today has not been completed. Please complete today\'s exercise.', 'Exercise Incomplete', '2024-05-29 17:12:18.079164', '2024-05-29', '17:12:18.079164', 0);

-- --------------------------------------------------------

--
-- Table structure for table `temp_resultex`
--

CREATE TABLE `temp_resultex` (
  `id` bigint NOT NULL,
  `rid` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `eid` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `result` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `date` date NOT NULL,
  `video_duration` double NOT NULL,
  `time` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `temp_resultex`
--

INSERT INTO `temp_resultex` (`id`, `rid`, `eid`, `result`, `date`, `video_duration`, `time`) VALUES
(12, '2981744854424', 'E07', '84.036', '2024-05-28', 27.415979, '19:32:07.256720'),
(19, '6556973175794', 'E03', '88.716', '2024-07-02', 27.416437, '12:23:01.038277'),
(20, '6556973175794', 'E03', '88.716', '2024-07-17', 27.416437, '12:03:11.876424'),
(22, '1426488133359', 'E07', '84.036', '2024-09-09', 38.437344, '00:38:24.958883'),
(24, '1426488133359', 'E07', '84.036', '2024-09-12', 41.417244, '15:54:12.140608'),
(25, '1426488133359', 'E07', '84.036', '2024-09-12', 32.788813, '15:56:24.591305'),
(45, '1426488133359', 'E07', '84.036', '2024-10-08', 30, '19:39:20.307710'),
(46, '1426488133359', 'E09', '88.020', '2024-10-08', 1702.626395, '19:40:46.171160'),
(47, '1426488133359', 'E08', '87.866', '2024-10-08', 19, '19:45:03.319908'),
(48, '1426488133359', 'E08', '88.020', '2024-10-08', 68.628271, '19:52:55.096715'),
(49, '1426488133359', 'E07', '84.036', '2025-03-15', 12, '14:14:49.727369');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authority_admin_list`
--
ALTER TABLE `authority_admin_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `doctor_doctordeactive`
--
ALTER TABLE `doctor_doctordeactive`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `DID` (`DID`);

--
-- Indexes for table `doctor_doctor_list`
--
ALTER TABLE `doctor_doctor_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `S_number` (`S_number`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `doctor_doctor_list_temp`
--
ALTER TABLE `doctor_doctor_list_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctor_doctor_patient_list`
--
ALTER TABLE `doctor_doctor_patient_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctor_exercise_list`
--
ALTER TABLE `doctor_exercise_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient_active_patient_list`
--
ALTER TABLE `patient_active_patient_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `RID` (`RID`);

--
-- Indexes for table `patient_disease_category`
--
ALTER TABLE `patient_disease_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient_patient_list`
--
ALTER TABLE `patient_patient_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `P_number` (`P_number`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `patient_patient_list_temp`
--
ALTER TABLE `patient_patient_list_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temp_noteexercise2`
--
ALTER TABLE `temp_noteexercise2`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temp_notification`
--
ALTER TABLE `temp_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `temp_notification_recipient_id_3f3d8566_fk_patient_p` (`recipient_id`);

--
-- Indexes for table `temp_notificationes2`
--
ALTER TABLE `temp_notificationes2`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temp_resultex`
--
ALTER TABLE `temp_resultex`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authority_admin_list`
--
ALTER TABLE `authority_admin_list`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `doctor_doctordeactive`
--
ALTER TABLE `doctor_doctordeactive`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `doctor_doctor_list`
--
ALTER TABLE `doctor_doctor_list`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `doctor_doctor_list_temp`
--
ALTER TABLE `doctor_doctor_list_temp`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `doctor_doctor_patient_list`
--
ALTER TABLE `doctor_doctor_patient_list`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `doctor_exercise_list`
--
ALTER TABLE `doctor_exercise_list`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `patient_active_patient_list`
--
ALTER TABLE `patient_active_patient_list`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `patient_disease_category`
--
ALTER TABLE `patient_disease_category`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `patient_patient_list`
--
ALTER TABLE `patient_patient_list`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `patient_patient_list_temp`
--
ALTER TABLE `patient_patient_list_temp`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `temp_noteexercise2`
--
ALTER TABLE `temp_noteexercise2`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `temp_notification`
--
ALTER TABLE `temp_notification`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `temp_notificationes2`
--
ALTER TABLE `temp_notificationes2`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `temp_resultex`
--
ALTER TABLE `temp_resultex`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `temp_notification`
--
ALTER TABLE `temp_notification`
  ADD CONSTRAINT `temp_notification_recipient_id_3f3d8566_fk_patient_p` FOREIGN KEY (`recipient_id`) REFERENCES `patient_patient_list` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
