-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: crawling_video
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Angular_videos`
--

DROP TABLE IF EXISTS `Angular_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Angular_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Angular_videos`
--

LOCK TABLES `Angular_videos` WRITE;
/*!40000 ALTER TABLE `Angular_videos` DISABLE KEYS */;
INSERT INTO `Angular_videos` VALUES ('Coating an Angular Jar with Crackle Glaze','https://www.youtube.com/shorts/ViQKfkXIQzI',5882435,'6개월 전'),('Angular Tutorial for Beginners: Learn Angular & TypeScript','https://www.youtube.com/watch?v=k5E2AVpwsko&pp=ygUHQW5ndWxhcg%3D%3D',3857035,'5년 전'),('Angular Vs Rounded Yoyos (Which Is Better?)','https://www.youtube.com/shorts/-fVJf138WVI',1307436,'2개월 전'),('Angular Tutorial in Hindi','https://www.youtube.com/watch?v=0LhBvp8qpro&pp=ygUHQW5ndWxhcg%3D%3D',1264117,'2년 전'),('Angular Crash Course','https://www.youtube.com/watch?v=3dHNOWTI7H8&pp=ygUHQW5ndWxhcg%3D%3D',1183576,'2년 전'),('Ionic 4 & Angular Tutorial For Beginners - Crash Course','https://www.youtube.com/watch?v=r2ga-iXS5i4&pp=ygUHQW5ndWxhcg%3D%3D',737501,'4년 전'),('Angular for Beginners Course [Full Front End Tutorial with TypeScript]','https://www.youtube.com/watch?v=3qBXWUpoPHo&pp=ygUHQW5ndWxhcg%3D%3D',662491,'7개월 전'),('Learn Angular 7 in 50 Minutes - A Free Beginner\'s Crash Course','https://www.youtube.com/watch?v=5wtnKulcquA&pp=ygUHQW5ndWxhcg%3D%3D',562615,'4년 전'),('Angular in 100 Seconds','https://www.youtube.com/watch?v=Ata9cSC2WpM&pp=ygUHQW5ndWxhcg%3D%3D',550503,'2년 전'),('Sharing Data between Components in Angular','https://www.youtube.com/watch?v=I317BhehZKM&pp=ygUHQW5ndWxhcg%3D%3D',453414,'6년 전');
/*!40000 ALTER TABLE `Angular_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_videos`
--

DROP TABLE IF EXISTS `app_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_videos`
--

LOCK TABLES `app_videos` WRITE;
/*!40000 ALTER TABLE `app_videos` DISABLE KEYS */;
INSERT INTO `app_videos` VALUES ('1년차 개발자 vs 5년차 개발자 #똑같다 #개발자 #코딩 #앱개발 #개발자유머 #코딩유머 #개발밈 #프로그래머','https://www.youtube.com/shorts/xLPwShqhL_I',794236,'1년 전'),('다음엔 무엇을 해볼까요? #채팅앱 #앱개발 #코딩 #chattingapp #chatbot #챗봇 #개발자브이로그','https://www.youtube.com/shorts/8Fl5rm-2Uvo',241232,'1년 전'),('앱개발, 10분만 투자하면 당신도 할 수 있습니다.','https://www.youtube.com/watch?v=oXxs8OAv4Xc&pp=ygUJ7JWx6rCc67Cc',161745,'12년 전'),('요즘 앱개발은 플러터로 해도 충분한듯 (플러터 설명과 장단점)','https://www.youtube.com/watch?v=JS-Si5GO3iA&pp=ygUJ7JWx6rCc67Cc',131016,'1년 전'),('앱개발로 스타트업이 100억 이상을 버는 방법 (어플개발, 어플광고, 말랑, 김영호대표)','https://www.youtube.com/watch?v=_8IPZI0pUwU&pp=ygUJ7JWx6rCc67Cc',104455,'3년 전'),('코딩으로 웹개발(앱개발)해서 돈벌어볼까?했던 사람들이 깨닫는것','https://www.youtube.com/watch?v=WJwEmork_tU&pp=ygUJ7JWx6rCc67Cc',64453,'2년 전'),('구글이 드디어 해냈구나… #flutter #앱개발','https://www.youtube.com/watch?v=d-MSD1MHn5w&pp=ygUJ7JWx6rCc67Cc',58965,'3개월 전'),('앱개발 할 때 처음부터 알면 좋았을 가장 중요한 2가지 + 아이디어만 있는 경우 어떻게 할지','https://www.youtube.com/watch?v=aDyv3kq_hlg&pp=ygUJ7JWx6rCc67Cc',48197,'1년 전'),('직접 만든 냉장고 관리 앱! 유통기한 정리 한방에?(앱개발,코딩,스타트업)','https://www.youtube.com/watch?v=xMjfA28KdmA&pp=ygUJ7JWx6rCc67Cc',44286,'1년 전'),('4강. 데이터 저장 및 관리 앱만들기 [앱개발, DB, 데이터베이스]','https://www.youtube.com/watch?v=bspkjnGPulE&pp=ygUJ7JWx6rCc67Cc',42989,'5년 전');
/*!40000 ALTER TABLE `app_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_videos`
--

DROP TABLE IF EXISTS `backend_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_videos`
--

LOCK TABLES `backend_videos` WRITE;
/*!40000 ALTER TABLE `backend_videos` DISABLE KEYS */;
INSERT INTO `backend_videos` VALUES ('프론트엔드? 백엔드? 진로고민 하시는 분은 보세요 | 개발자 직군별 차이, 성향, 연봉','https://www.youtube.com/watch?v=S9qAtvvvxio&pp=ygUJ67Cx7JeU65Oc',349207,'1년 전'),('판교 개발자의 이상적인 삶?! ?‍? 카카오 백엔드 개발자의 하루 그 잡채!ㅣ카카오 크루 Vlog','https://www.youtube.com/watch?v=1Z-VTp4H2Wk&pp=ygUJ67Cx7JeU65Oc',175489,'9개월 전'),('알아두면 깜놀! 넷플릭스 백엔드의 진실!?','https://www.youtube.com/watch?v=_DDkSF5TvEU&pp=ygUJ67Cx7JeU65Oc',130487,'1년 전'),('비전공자도 백엔드 개발자 합격했어요! [백엔드 스쿨]','https://www.youtube.com/watch?v=WiLnnZYj7gY&pp=ygUJ67Cx7JeU65Oc',122879,'7개월 전'),('비전공자도 백엔드 개발자 합격했어요! [백엔드 스쿨]','https://www.youtube.com/watch?v=WiLnnZYj7gY&pp=ygUJ67Cx7JeU65Oc',122879,'7개월 전'),('프론트엔드 개발자 백엔드 개발자 무엇을 선택할까? 공부 방법은? (Frontend vs Backend)','https://www.youtube.com/watch?v=-y9h5yl7egE&pp=ygUJ67Cx7JeU65Oc',113445,'2년 전'),('한시간만에 Node.js 백엔드 기초 끝내기 (ft. API 구축)','https://www.youtube.com/watch?v=Tt_tKhhhJqY&pp=ygUJ67Cx7JeU65Oc',104738,'5개월 전'),('프론트엔드 백엔드 개발자는 무슨일을 하나요?','https://www.youtube.com/watch?v=G7crMao49_I&pp=ygUJ67Cx7JeU65Oc',101317,'3년 전'),('백엔드 공부 순서 | 백엔드 개발자가 되려면 뭘 공부해야 할까?','https://www.youtube.com/watch?v=89bFo003oik&pp=ygUJ67Cx7JeU65Oc',98519,'2년 전'),('프론트엔드,백엔드 차이점ㅋㅋㅋ엌ㅋㅋㅋㅋ','https://www.youtube.com/shorts/AZlWbtt0sG4',90502,'4주 전');
/*!40000 ALTER TABLE `backend_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cert_videos`
--

DROP TABLE IF EXISTS `cert_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cert_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cert_videos`
--

LOCK TABLES `cert_videos` WRITE;
/*!40000 ALTER TABLE `cert_videos` DISABLE KEYS */;
INSERT INTO `cert_videos` VALUES ('[인터뷰] S사 정보보안관제 팀장님을 만나다.(솔직주의. 아무말이나 해도 괜찮겠습니까?) 취업 노하우 공개!','https://www.youtube.com/watch?v=a8kQztzFZEw&pp=ygUM67O07JWI6rSA7KCc',21696,'3년 전'),('[인생첫직] 정보보안전문가 중 가장 많이 채용하는 보안관제 직무설명','https://www.youtube.com/watch?v=XdZPVD_D8GM&pp=ygUM67O07JWI6rSA7KCc',12359,'2년 전'),('보안관제 전문가는 무슨일을 하나요??','https://www.youtube.com/watch?v=FoOJ9nZ5Ssc&pp=ygUM67O07JWI6rSA7KCc',7282,'4년 전'),('보안관제 업무는 장비 모니터링만 하는 곳이 아니다.','https://www.youtube.com/watch?v=nEWqu4hLZlg&pp=ygUM67O07JWI6rSA7KCc',5023,'3년 전'),('보안관제 기준 \'이글루시큐리티\'','https://www.youtube.com/watch?v=GtKr6tO_rHE&pp=ygUM67O07JWI6rSA7KCc',4949,'11년 전'),('보안관제 회사는 어떻게 해킹을 탐지하고 방어할까?','https://www.youtube.com/watch?v=ebOGw7xKMko&pp=ygUM67O07JWI6rSA7KCc',4872,'3년 전'),('시큐레이어 (SecuLayer) 회사 소개 - 통합보안관제솔루션의 리더 SOAR, SIEM, 인공지능플랫폼','https://www.youtube.com/watch?v=yb_XW4g-48U&pp=ygUM67O07JWI6rSA7KCc',4565,'1년 전'),('(IT보안 강의) 보안관제와 침해대응 업무의 이해','https://www.youtube.com/watch?v=YmpuiKxvQ58&pp=ygUM67O07JWI6rSA7KCc',4201,'4년 전'),('정보보안관제','https://www.youtube.com/watch?v=Q4yTSALjoGI&pp=ygUM67O07JWI6rSA7KCc',3502,'6년 전'),('AhnLab 보안관제서비스 (Kor)','https://www.youtube.com/watch?v=GotcQIaeA-I&pp=ygUM67O07JWI6rSA7KCc',3194,'4년 전');
/*!40000 ALTER TABLE `cert_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLanguage_videos`
--

DROP TABLE IF EXISTS `CLanguage_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CLanguage_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLanguage_videos`
--

LOCK TABLES `CLanguage_videos` WRITE;
/*!40000 ALTER TABLE `CLanguage_videos` DISABLE KEYS */;
INSERT INTO `CLanguage_videos` VALUES ('C언어 기초 프로그래밍 강좌 1강 - Hello World (C Programming Tutorial For Beginners 2017 #1)','https://www.youtube.com/watch?v=dh4hdtZ00EU&pp=ygUHQ-yWuOyWtA%3D%3D',707721,'6년 전'),('C언어 기초 프로그래밍 강좌 2강 - 변수와 상수(Variables & Constants) (C Programming Tutorial For Beginners 2017 #2)','https://www.youtube.com/watch?v=V7TXlm7kpaE&pp=ygUHQ-yWuOyWtA%3D%3D',283965,'6년 전'),('[혼공C_새로워진 이것이 C언어다] 1강. 01-1 프로그램과 C언어 / 01-2 컴파일러 사용법','https://www.youtube.com/watch?v=wWJ3koUPPG4&pp=ygUHQ-yWuOyWtA%3D%3D',204945,'8년 전'),('동영상 강좌 - \'Do it! C언어 입문\' - 1장','https://www.youtube.com/watch?v=flszoDfgwjc&pp=ygUHQ-yWuOyWtA%3D%3D',99849,'5년 전'),('영어영문학과가 C언어를 배우는방법','https://www.youtube.com/watch?v=TbKdf2wTojk&pp=ygUHQ-yWuOyWtA%3D%3D',86546,'2년 전'),('29살의 C언어 with 거니 [Chapter#9 - 포인터]','https://www.youtube.com/watch?v=A7C9-Ea_zBQ&pp=ygUHQ-yWuOyWtA%3D%3D',73453,'3년 전'),('C언어 알고리즘 기초 100제 함께 풀어보아요! (C언어 스터디) [1번 ~ 40번]','https://www.youtube.com/watch?v=mY1-xSmJEic&pp=ygUHQ-yWuOyWtA%3D%3D',61566,'스트리밍 시간: 4년 전'),('C언어 – 문법 기초','https://www.youtube.com/watch?v=I2giEjUHe0M&pp=ygUHQ-yWuOyWtA%3D%3D',52607,'2년 전'),('[맨처음 C언어 기초 2시간 완성] C언어 공부를 맨처음 시작하는 분들을 위한 입문강의','https://www.youtube.com/watch?v=ueYLF0NIHkE&pp=ygUHQ-yWuOyWtA%3D%3D',47917,'10개월 전'),('코딩공부 작심삼일 실패하는 이유 (파이썬,C언어 먼저하면 망함) 부트캠프 강사가 알려주는 코딩 공부법, 코딩 독학하는 이들을 위한 영상','https://www.youtube.com/watch?v=_8mjcJAp0Sw&pp=ygUHQ-yWuOyWtA%3D%3D',43455,'1년 전');
/*!40000 ALTER TABLE `CLanguage_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotlin_videos`
--

DROP TABLE IF EXISTS `cotlin_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cotlin_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotlin_videos`
--

LOCK TABLES `cotlin_videos` WRITE;
/*!40000 ALTER TABLE `cotlin_videos` DISABLE KEYS */;
INSERT INTO `cotlin_videos` VALUES ('한국인을 위한 안드로이드 스튜디오 코틀린 백과사전','https://www.youtube.com/watch?v=WlJszSmK_es&pp=ygUJ7L2U7YuA66aw',893095,'2년 전'),('코틀린이 자바를 대체할 수 있을까? 6분 제대로 이해하기!','https://www.youtube.com/watch?v=8gseVzeMOzk&pp=ygUJ7L2U7YuA66aw',113123,'3년 전'),('코틀린 3강으로 끝내기 - 1편 기본 문법 | #안드로이드 #코틀린강의','https://www.youtube.com/watch?v=IDVnZPjRCYg&pp=ygUJ7L2U7YuA66aw',101116,'3년 전'),('Kotlin 강좌 #1 - 코틀린의 시작','https://www.youtube.com/watch?v=8RIsukgeUVw&pp=ygUJ7L2U7YuA66aw',86507,'3년 전'),('[코틀린 안드로이드 기초 강의_1] Android 스튜디오 설치하기','https://www.youtube.com/watch?v=2qs9vCYwufs&pp=ygUJ7L2U7YuA66aw',44955,'2년 전'),('코틀린 3강으로 끝내기 - 3편 심리테스트 앱 만들기 | #안드로이드 #코틀린','https://www.youtube.com/watch?v=M1e2tLnzVPo&pp=ygUJ7L2U7YuA66aw',37493,'2년 전'),('[센치한 개발자] (25) 안드로이드 코틀린 기초 강좌 : 코틀린(Kotlin) 기초문법, 예제 설명 - 1','https://www.youtube.com/watch?v=GcIkrq-mwtg&pp=ygUJ7L2U7YuA66aw',33073,'3년 전'),('코틀린 3강으로 끝내기 - 2편 고급 문법 | #안드로이드 #코틀린강의','https://www.youtube.com/watch?v=Q5noYbbc9uc&pp=ygUJ7L2U7YuA66aw',27521,'3년 전'),('안드로이드개발 시작하기 / 초보개발자 / 기본 튜토리얼 / 코틀린 / 앱만들기','https://www.youtube.com/watch?v=32SGwgbUSYw&pp=ygUJ7L2U7YuA66aw',23196,'3년 전'),('바로 말씀 드릴께요. 자바 vs 코틀린 java vs kotlin 차이 비교 선택 시 고려 사항','https://www.youtube.com/watch?v=qFxQpq_yYnE&pp=ygUJ7L2U7YuA66aw',22828,'2년 전');
/*!40000 ALTER TABLE `cotlin_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_videos`
--

DROP TABLE IF EXISTS `django_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_videos`
--

LOCK TABLES `django_videos` WRITE;
/*!40000 ALTER TABLE `django_videos` DISABLE KEYS */;
INSERT INTO `django_videos` VALUES ('초보자를 위한 Python Django 튜토리얼','https://www.youtube.com/watch?v=rHux0gMZ3Eg&pp=ugMICgJrbxABGAHKBQ1QeXRob24gRGphbmdv',1566215,'1년 전'),('Python Django 7시간 코스','https://www.youtube.com/watch?v=PtQiiknWUcI&pp=ugMICgJrbxABGAHKBQ1QeXRob24gRGphbmdv',1059573,'1년 전'),('Creating Our First Django Project | Python Django Tutorials In Hindi #2','https://www.youtube.com/watch?v=weAUmhABjBc&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',410348,'4년 전'),('Python Django Web Framework - 1/14. 수업소개','https://www.youtube.com/watch?v=pbKhn2ten9I&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',47878,'1년 전'),('Python Django Web Framework - 2/14. 설치','https://www.youtube.com/watch?v=xGdUNyVkAto&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',25989,'1년 전'),('Complete Django Course for 2023 - Zero to Hero in Python Django | Python Django Tutorial','https://www.youtube.com/watch?v=Mezody4yiXw&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',8047,'2개월 전'),('Create Python Django apps with GitHub Copilot','https://www.youtube.com/watch?v=HDsJQVa0R94&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',6606,'4주 전'),('?밑바닥 부터 시작하는 파이썬 장고 Python Django From Scratch','https://www.youtube.com/watch?v=an89p2xXREU&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',4122,'2년 전'),('0.기초부터 제작하는 파이썬 장고(Python Django) 프로젝트  - 강의 안내','https://www.youtube.com/watch?v=0cPTL6ct8yo&pp=ygUNUHl0aG9uIERqYW5nbw%3D%3D',4114,'2년 전'),('Best Youtube Channel for Python Django - Advanced  Topics #django','https://www.youtube.com/shorts/7qB6Swha0Cc',3755,'2개월 전');
/*!40000 ALTER TABLE `django_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flask_videos`
--

DROP TABLE IF EXISTS `flask_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flask_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flask_videos`
--

LOCK TABLES `flask_videos` WRITE;
/*!40000 ALTER TABLE `flask_videos` DISABLE KEYS */;
INSERT INTO `flask_videos` VALUES ('Python Flask From Scratch - [Part 1] - Getting Started','https://www.youtube.com/watch?v=zRwy8gtgJ1A&pp=ygUMUHl0aG9uIEZsYXNr',499390,'6년 전'),('Python Flask Tutorial For Beginners | Flask Web Development Tutorial | Python Training | Edureka','https://www.youtube.com/watch?v=lj4I_CvBnt0&pp=ygUMUHl0aG9uIEZsYXNr',211316,'4년 전'),('Full stack Python Flask tutorial - Build a social network','https://www.youtube.com/watch?v=-FWuNnCe73g&pp=ygUMUHl0aG9uIEZsYXNr',141697,'4년 전'),('Convert Python Flask APP to Docker Container | Docker | Python Flask','https://www.youtube.com/watch?v=prlixoDIfrc&pp=ygUMUHl0aG9uIEZsYXNr',112060,'4년 전'),('Python Flask, React Hooks  & MongoDB CRUD','https://www.youtube.com/watch?v=D1W8H4Rkb9A&pp=ygUMUHl0aG9uIEZsYXNr',53554,'3년 전'),('Image Editing Website using Python Flask and OpenCV','https://www.youtube.com/watch?v=hVEZYEYctSc&pp=ygUMUHl0aG9uIEZsYXNr',20134,'11일 전'),('Python Flask Tutorial #2 - Routing','https://www.youtube.com/watch?v=EMcTreG8N3g&pp=ygUMUHl0aG9uIEZsYXNr',18697,'4년 전'),('Flask Interview Questions and Answers | Python Flask | Flask Basics | Flask FAQ |','https://www.youtube.com/watch?v=-qydLpQxa6Y&pp=ygUMUHl0aG9uIEZsYXNr',10773,'2년 전'),('Python Flask Tutorial - FULL COURSE (2023)','https://www.youtube.com/watch?v=2YOBmELm_v0&pp=ygUMUHl0aG9uIEZsYXNr',8520,'3개월 전'),('Python Flask Tutorial #9 - Cookies','https://www.youtube.com/watch?v=w5CgRaBVZ7c&pp=ygUMUHl0aG9uIEZsYXNr',6882,'4년 전');
/*!40000 ALTER TABLE `flask_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flutter_videos`
--

DROP TABLE IF EXISTS `flutter_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flutter_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flutter_videos`
--

LOCK TABLES `flutter_videos` WRITE;
/*!40000 ALTER TABLE `flutter_videos` DISABLE KEYS */;
INSERT INTO `flutter_videos` VALUES ('요즘 앱개발은 플러터로 해도 충분한듯 (플러터 설명과 장단점)','https://www.youtube.com/watch?v=JS-Si5GO3iA&pp=ygUJ7ZSM65-s7YSw',131039,'1년 전'),('플러터(flutter) 순한맛 강좌 1 | 우리는 왜 플러터(flutter)를 학습해야 할까요?','https://www.youtube.com/watch?v=AdYRASHRKwE&pp=ygUJ7ZSM65-s7YSw',92791,'3년 전'),('플러터로 게임만들었는데 생각보다 좋음','https://www.youtube.com/watch?v=9t1oGuaaEz4&pp=ygUJ7ZSM65-s7YSw',88159,'3개월 전'),('쉬운 플러터 0강 : 플러터 설치 4-step (맥/윈도우)','https://www.youtube.com/watch?v=usE9IKaogDU&pp=ygUJ7ZSM65-s7YSw',73410,'1년 전'),('쉬운 플러터 0강 : 플러터 설치 4-step (맥/윈도우)','https://www.youtube.com/watch?v=usE9IKaogDU&pp=ygUJ7ZSM65-s7YSw',73410,'1년 전'),('쉬운 플러터 1강 : 기본 위젯4개 알면 기초 끝','https://www.youtube.com/watch?v=mLQ-ehf3d6Y&pp=ygUJ7ZSM65-s7YSw',65534,'1년 전'),('플러터 VS 리액트 네이티브, 2023년의 승자는?','https://www.youtube.com/watch?v=Z9cCjrbTW50&pp=ygUJ7ZSM65-s7YSw',52660,'2개월 전'),('쉬운 플러터 2강 : 가로세로 배치하는 법과 Scaffold','https://www.youtube.com/watch?v=U6rLIFn59Kw&pp=ygUJ7ZSM65-s7YSw',34587,'1년 전'),('쉬운 플러터 3강 : 박스잘그려야 앱잘만듭니다','https://www.youtube.com/watch?v=4KH4_6Gd6sE&pp=ygUJ7ZSM65-s7YSw',29297,'1년 전'),('플러터(flutter) 순한 맛 강좌 8 | 플러터 앱페이지 기본 코드 이해하기 3 (완결편)','https://www.youtube.com/watch?v=AXFV1JOr6_Q&pp=ygUJ7ZSM65-s7YSw',28551,'3년 전');
/*!40000 ALTER TABLE `flutter_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontend_videos`
--

DROP TABLE IF EXISTS `frontend_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frontend_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontend_videos`
--

LOCK TABLES `frontend_videos` WRITE;
/*!40000 ALTER TABLE `frontend_videos` DISABLE KEYS */;
INSERT INTO `frontend_videos` VALUES ('프론트엔드? 백엔드? 진로고민 하시는 분은 보세요 | 개발자 직군별 차이, 성향, 연봉','https://www.youtube.com/watch?v=S9qAtvvvxio&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',349225,'1년 전'),('\'9X년생 개발자\'가 연봉 50% 올린 방법은? 제플의 프론트엔드 엔지니어 진유림','https://www.youtube.com/watch?v=80t4PlCuS68&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',284875,'3년 전'),('웹 프론트엔드 개발자 아무것도 모르는 상태에서 취업까지 하는 구체적인 준비방법 | 프론트엔드 공부순서 | 취업준비 | 면접준비','https://www.youtube.com/watch?v=YbVuqWD12Ko&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',132628,'2년 전'),('신입 웹 프론트엔드 개발자의 데스크 셋업','https://www.youtube.com/watch?v=kmr3iuOtA8A&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',132136,'2년 전'),('프론트엔드 개발자 백엔드 개발자 무엇을 선택할까? 공부 방법은? (Frontend vs Backend)','https://www.youtube.com/watch?v=-y9h5yl7egE&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',113447,'2년 전'),('프론트엔드 백엔드 개발자는 무슨일을 하나요?','https://www.youtube.com/watch?v=G7crMao49_I&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',101323,'3년 전'),('프론트엔드,백엔드 차이점ㅋㅋㅋ엌ㅋㅋㅋㅋ','https://www.youtube.com/shorts/AZlWbtt0sG4',90542,'4주 전'),('(Next.js 0강) 요즘 프론트엔드만으로 먹고살기 힘든 이유','https://www.youtube.com/watch?v=jYJ3ygUfPrU&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',89894,'3주 전'),('프론트엔드 개발자 vs 백엔드 개발자 (Frontend vs Backend)','https://www.youtube.com/watch?v=oOd0IKWwg1E&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',86348,'4년 전'),('이거 모르면 프론트엔드 개발자 못됨 | 리액트 진짜 쉽게 설명해줌 | 리액트 초보자 입문 강의 1탄','https://www.youtube.com/watch?v=MeZ3FCTub3I&pp=ygUP7ZSE66Gg7Yq47JeU65Oc',82624,'1년 전');
/*!40000 ALTER TABLE `frontend_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hacker_videos`
--

DROP TABLE IF EXISTS `hacker_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hacker_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hacker_videos`
--

LOCK TABLES `hacker_videos` WRITE;
/*!40000 ALTER TABLE `hacker_videos` DISABLE KEYS */;
INSERT INTO `hacker_videos` VALUES ('전직해커 현개발자 인증한다! 모의해킹사이트 뚫기!  [개발자와 떠나는 진짜 딥웹탐사 - 청일TV]','https://www.youtube.com/watch?v=YMWP5u5V8q0&pp=ygUM66qo7J2Y7ZW07YK5',17591,'4년 전'),('(칼리리눅스, 모의해킹) 칼리리눅스 기본명령어, 첫번째','https://www.youtube.com/watch?v=kKmtX7LVZak&pp=ygUM66qo7J2Y7ZW07YK5',16686,'4년 전'),('백트랙을 활용한 모의해킹 강의 01 - 모의해킹의 정의','https://www.youtube.com/watch?v=UsO9Rx1Z9Yw&pp=ygUM66qo7J2Y7ZW07YK5',11893,'9년 전'),('(버프스위트를 활용한 웹 모의해킹 시리즈) 01 버프스위트 설치 및 기능요약설명','https://www.youtube.com/watch?v=hZneBKxSbsw&pp=ygUM66qo7J2Y7ZW07YK5',10915,'5년 전'),('CIDISK 보안영역 모의해킹 시연( Simulated Hacking Demonstration Video )','https://www.youtube.com/watch?v=EW29gBDTr44&pp=ygUM66qo7J2Y7ZW07YK5',8862,'6년 전'),('정보보안기사 웹취약점 및 모의해킹 특강1편','https://www.youtube.com/watch?v=q-xmMmKMrdI&pp=ygUM66qo7J2Y7ZW07YK5',8426,'2년 전'),('[화이트해커] 왜 모의해킹을 배워야할까: 4차 산업혁명 시대 장래희망 직업 - 정보보안전문가','https://www.youtube.com/watch?v=ranHyXZQBhE&pp=ygUM66qo7J2Y7ZW07YK5',7667,'4년 전'),('모의해킹 오래 못하는 3가지 유형 | 화이트 해커의 수명은 짧다? | 화이트 해커 진로 고민 시 필수 시청 영상','https://www.youtube.com/watch?v=gLvulUx3Eek&pp=ygUM66qo7J2Y7ZW07YK5',6842,'6개월 전'),('모의해킹 취업이 어렵다고??? | 모의해킹 취업반 3기 모집! | 5개월간 같이 달려보자!!!','https://www.youtube.com/watch?v=zpHP86K0zoY&pp=ygUM66qo7J2Y7ZW07YK5',6632,'7개월 전'),('(해킹, 보안) 모의해킹 동적분석 이해 및 활용도구','https://www.youtube.com/watch?v=t8RFyDGprQ4&pp=ygUM66qo7J2Y7ZW07YK5',5762,'4년 전');
/*!40000 ALTER TABLE `hacker_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interview_videos`
--

DROP TABLE IF EXISTS `interview_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interview_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interview_videos`
--

LOCK TABLES `interview_videos` WRITE;
/*!40000 ALTER TABLE `interview_videos` DISABLE KEYS */;
INSERT INTO `interview_videos` VALUES ('위 수식이 틀린 이유는? (개발자 면접 타임)','https://www.youtube.com/watch?v=-GsrYvZoAdA&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',877838,'8개월 전'),('요즘 개쉬워진 개발자 면접?‍? (마지막ㅋㅋㅋㅋ) #Shorts','https://www.youtube.com/shorts/jGIAVrEkZ9U',867707,'1개월 전'),('면접관은 도대체 무슨 생각을 할까? | 신입 개발자 면접 질문 & 질문 의도 & 답변 예시','https://www.youtube.com/watch?v=7ye03TMi5SU&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',118365,'2년 전'),('[뚜데] #6 백엔드 개발자 면접관으로 들어가서 느낀점, 팁, 썰 풉니다.','https://www.youtube.com/watch?v=gXfEE6v5bSI&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',70550,'1년 전'),('국비지원 경력만으로 ㅈㄴ 좋은회사간 친구를 만났습니다 | 신입 개발자 면접 잘보는법 2탄','https://www.youtube.com/watch?v=XXX0VttsjAw&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',45569,'1년 전'),('개발자 면접 단골질문 자바스크립트 this','https://www.youtube.com/watch?v=tDZROpAdJ9w&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',39754,'4개월 전'),('시니어 개발자들은 보지마세요. 신입 or 주니어 개발자 면접 꿀팁 1탄 - 코딩테스트, 코딩 면접 잘보는 법','https://www.youtube.com/watch?v=HFEurBNmMwM&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',23129,'1년 전'),('너무 당돌했던 백엔드 취준생의 중소기업 첫 면접 후기? (합격 후기) | 개발자 면접','https://www.youtube.com/watch?v=PMsB__J9rbc&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',21930,'1년 전'),('개발자 면접자리에서 받은 질문들 (자바,스프링)','https://www.youtube.com/watch?v=FP6yuNH1bNE&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',20609,'3년 전'),('기술면접 모르는 질문 받았을때 대처법 | 시니어 개발자 분들은 보지 마세요 | 신입개발자, 주니어 개발자 면접 꿀팁','https://www.youtube.com/watch?v=4XNJFAPnZrY&pp=ygUQ6rCc67Cc7J6QIOuptOygkQ%3D%3D',16374,'1년 전');
/*!40000 ALTER TABLE `interview_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `it_trend_videos`
--

DROP TABLE IF EXISTS `it_trend_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `it_trend_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `it_trend_videos`
--

LOCK TABLES `it_trend_videos` WRITE;
/*!40000 ALTER TABLE `it_trend_videos` DISABLE KEYS */;
INSERT INTO `it_trend_videos` VALUES ('미국이 주목하는 올해 IT 트렌드는?','https://www.youtube.com/watch?v=MYVc9_z7Jz4&pp=ygUMSVQg7Yq466CM65Oc',11173,'10년 전'),('모바일을 사용하는 모든 이들을 위한 커넥팅랩의 IT 트렌드서 | 모바일 미래보고서 2022','https://www.youtube.com/watch?v=qtklYyPtSLA&pp=ygUMSVQg7Yq466CM65Oc',10732,'1년 전'),('올해 IT 트렌드는... 웨어러블 시대 열릴 것','https://www.youtube.com/watch?v=-u1mHd7cH94&pp=ygUMSVQg7Yq466CM65Oc',7980,'9년 전'),('[IT Plus] 2022년 제야의 종은 ‘이 곳’ 에서 열린다고?! 5가지 키워드로 알아보는 지금 주목할 IT 트렌드? | 2021 · 2022년 IT 트렌드 요약부터 전망까지','https://www.youtube.com/watch?v=DC0mUqhQBSQ&pp=ygUMSVQg7Yq466CM65Oc',7374,'1년 전'),('2023년 IT 트렌드를 찍먹해 보자! (feat. 가트너)','https://www.youtube.com/watch?v=w6sepP8xnaY&pp=ygUMSVQg7Yq466CM65Oc',2950,'4개월 전'),('2022 IT 트렌드 관련 책 리뷰 | 1일 1로그 100일완성 IT지식, 그림으로 이해하는 IT 지식과 트렌드, 비전공자도 이해할 수 있는 AI 지식','https://www.youtube.com/watch?v=w0l9tXefE0M&pp=ygUMSVQg7Yq466CM65Oc',2478,'7개월 전'),('IT 트렌드의 변화? 아마존, 마이크로소프트, 애플, 페이스북, 퀄컴, AMD 실적 리뷰 그리고 전망 (feat. 베가스풍류객)','https://www.youtube.com/watch?v=mLJq1vhib24&pp=ygUMSVQg7Yq466CM65Oc',1846,'4년 전'),('[JOB CAST] IT 직무소개부터 IT 트렌드까지! 가구회사 IT 전문가들의 직무 ON&OFF? | 퍼시스그룹 | IT직군','https://www.youtube.com/watch?v=ltqwNsc1Us8&pp=ygUMSVQg7Yq466CM65Oc',1534,'1년 전'),('금융 IT 트렌드, 올해의 전망은?','https://www.youtube.com/watch?v=NHyfG12Jog8&pp=ygUMSVQg7Yq466CM65Oc',1350,'4년 전'),('[유노IT] 2025년 IT 트렌드 (1/6) - 프로세스 자동화와 가상화 | In 2025, IT trends (1/6) - Process Automation','https://www.youtube.com/shorts/0L08-wy8MC4',1235,'11일 전');
/*!40000 ALTER TABLE `it_trend_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `java_videos`
--

DROP TABLE IF EXISTS `java_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `java_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `java_videos`
--

LOCK TABLES `java_videos` WRITE;
/*!40000 ALTER TABLE `java_videos` DISABLE KEYS */;
INSERT INTO `java_videos` VALUES ('자바 풀코스 무료 ☕','https://www.youtube.com/watch?v=xk4_1vDrzzo&pp=ugMICgJrbxABGAHKBQbsnpDrsJQ%3D',6734192,'2년 전'),('자바스크립트 기초 강좌 : 100분 완성','https://www.youtube.com/watch?v=KF6t61yuPCY&pp=ygUG7J6Q67CU',376913,'2년 전'),('자바 수업을 리뉴얼 했습니다','https://www.youtube.com/watch?v=jdTsJzXmgU0&pp=ygUG7J6Q67CU',344496,'2년 전'),('자바스크립트 특 ㅋㅋㅋㅋ #Shorts','https://www.youtube.com/shorts/owZ6oNzcJR0',196358,'6개월 전'),('자바 코딩 무료 강의 (기본편) - 9시간 뒤면 여러분도 개발자가 될 수 있어요','https://www.youtube.com/watch?v=NQq0dOoEPUM&pp=ygUG7J6Q67CU',161619,'4개월 전'),('코딩/프로그래밍 처음 하는 사람이 배우기 제일 좋은 언어는? - C언어, 자바, 파이썬, 자바스크립트, 루비 비교','https://www.youtube.com/watch?v=Wbjc8qAqHaI&pp=ygUG7J6Q67CU',151072,'3년 전'),('코틀린이 자바를 대체할 수 있을까? 6분 제대로 이해하기!','https://www.youtube.com/watch?v=8gseVzeMOzk&pp=ygUG7J6Q67CU',113127,'3년 전'),('왜 자바스크립트는 현재 가장 유명한 프로그래밍 언어일까?','https://www.youtube.com/watch?v=NMHQkAS7XEc&pp=ygUG7J6Q67CU',112958,'3년 전'),('자바스크립트 기초 입문 강의 30분 완성','https://www.youtube.com/watch?v=E-PzX2mKGUQ&pp=ygUG7J6Q67CU',99184,'6개월 전'),('자바 공부 어떻게 해야하나요? 책, 강의, 스터디 방식! 추천 드립니다.','https://www.youtube.com/watch?v=6gNMsjcH3oA&pp=ygUG7J6Q67CU',93847,'2년 전');
/*!40000 ALTER TABLE `java_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jQuery_videos`
--

DROP TABLE IF EXISTS `jQuery_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jQuery_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jQuery_videos`
--

LOCK TABLES `jQuery_videos` WRITE;
/*!40000 ALTER TABLE `jQuery_videos` DISABLE KEYS */;
INSERT INTO `jQuery_videos` VALUES ('jQuery Tutorial For Beginners In Hindi - हिंदी में','https://www.youtube.com/watch?v=YFlx1C8XwR0&pp=ygUGalF1ZXJ5',451697,'4년 전'),('jQuery','https://www.youtube.com/watch?v=8mwKq7_JlS8&pp=ygUGalF1ZXJ5',330956,'15년 전'),('100초 안에 jQuery의 전설','https://www.youtube.com/watch?v=UU-GebNqdbg&pp=ugMICgJrbxABGAHKBQZqUXVlcnk%3D',329658,'2년 전'),('jQuery Introduction Tutorial in Hindi / Urdu','https://www.youtube.com/watch?v=QvaFeU0LWnc&pp=ygUGalF1ZXJ5',316586,'4년 전'),('jQuery Tutorial For Beginners | Developing User Interface (UI) Using jQuery | Edureka','https://www.youtube.com/watch?v=2OMzGhlIZpg&pp=ygUGalF1ZXJ5',224739,'4년 전'),('jQuery in One Video in Hindi 2019','https://www.youtube.com/watch?v=PNvyPEQ0y-I&pp=ygUGalF1ZXJ5',169886,'4년 전'),('(ENG SUB)[Javascript 기초와 활용 #1]  완전 쉬운 jQuery로 스타크래프트 만들기?!','https://www.youtube.com/watch?v=z2Cu7gPMq0w&pp=ygUGalF1ZXJ5',165879,'3년 전'),('2: How to add jQuery to your website | Learn jQuery | jQuery tutorial','https://www.youtube.com/watch?v=EwUOsRlDTLQ&pp=ygUGalF1ZXJ5',152294,'6년 전'),('JQUERY Tutorial Español - ? Curso de jQuery 2018 desde cero ?','https://www.youtube.com/watch?v=DVN8NWppCN0&pp=ygUGalF1ZXJ5',135242,'4년 전'),('jQuery Basic Syntax Tutorial in Hindi / Urdu','https://www.youtube.com/watch?v=wjFfyqEutYE&pp=ygUGalF1ZXJ5',126196,'4년 전');
/*!40000 ALTER TABLE `jQuery_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodejs_videos`
--

DROP TABLE IF EXISTS `nodejs_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nodejs_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodejs_videos`
--

LOCK TABLES `nodejs_videos` WRITE;
/*!40000 ALTER TABLE `nodejs_videos` DISABLE KEYS */;
INSERT INTO `nodejs_videos` VALUES ('초보자를 위한 Node.js 튜토리얼: 1시간 만에 노드 배우기','https://www.youtube.com/watch?v=TlB_eWDSMt4&pp=ugMICgJrbxABGAHKBQdOb2RlLmpz',4998115,'5년 전'),('초보자를 위한 Node.js 튜토리얼: 1시간 만에 노드 배우기','https://www.youtube.com/watch?v=TlB_eWDSMt4&pp=ugMICgJrbxABGAHKBQdOb2RlLmpz',4998115,'5년 전'),('Node.js 및 Express.js - 전체 과정','https://www.youtube.com/watch?v=Oe421EPjeBE&pp=ugMICgJrbxABGAHKBQdOb2RlLmpz',2309218,'2년 전'),('Node.js 단기집중과정','https://www.youtube.com/watch?v=fBNz5xF-Kx4&pp=ugMICgJrbxABGAHKBQdOb2RlLmpz',1451134,'4년 전'),('Node.js 궁극의 초보자 가이드 7단계','https://www.youtube.com/watch?v=ENrzD9HAZK4&pp=ugMICgJrbxABGAHKBQdOb2RlLmpz',1130959,'2년 전'),('Node.js / Express 과정 - 4개의 프로젝트 빌드','https://www.youtube.com/watch?v=qwfE7fSVaZM&pp=ugMICgJrbxABGAHKBQdOb2RlLmpz',890986,'1년 전'),('React & Node.js ИНТЕРНЕТ МАГАЗИН С НУЛЯ. PERN stack PostgreSQL + express + React js + node.js','https://www.youtube.com/watch?v=H2GCkRF9eko&pp=ygUHTm9kZS5qcw%3D%3D',704267,'2년 전'),('Node.js Crash Course Tutorial #1 - Introduction & Setup','https://www.youtube.com/watch?v=zb3Qk8SG5Ms&pp=ygUHTm9kZS5qcw%3D%3D',625172,'2년 전'),('What is Node js? | Simplified Explanation','https://www.youtube.com/watch?v=yEHCfRWz-EI&pp=ygUHTm9kZS5qcw%3D%3D',603051,'3년 전'),('What is Node js? | Simplified Explanation','https://www.youtube.com/watch?v=yEHCfRWz-EI&pp=ygUHTm9kZS5qcw%3D%3D',603051,'3년 전');
/*!40000 ALTER TABLE `nodejs_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `python_videos`
--

DROP TABLE IF EXISTS `python_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `python_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `python_videos`
--

LOCK TABLES `python_videos` WRITE;
/*!40000 ALTER TABLE `python_videos` DISABLE KEYS */;
INSERT INTO `python_videos` VALUES ('파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]','https://www.youtube.com/watch?v=kWiCuklohdY&pp=ygUJ7YyM7J207I2s',4538085,'3년 전'),('파이썬 코딩 무료 강의 (활용편1) - 추억의 오락실 게임을 만들어 보아요. 3시간이면 충분합니다. [나도코딩]','https://www.youtube.com/watch?v=Dkx8Pl6QKW0&pp=ygUJ7YyM7J207I2s',2856664,'3년 전'),('파이썬 코딩 무료 강의 (활용편2) - GUI 프로그래밍을 배우고 \'여러 이미지 합치기\' 프로그램을 함께 만들어요. [나도코딩]','https://www.youtube.com/watch?v=bKPIcoou9N8&pp=ygUJ7YyM7J207I2s',1306414,'2년 전'),('최신 파이썬 코딩 무료 강의 - 5시간만 투자하면 개발자가 됩니다','https://www.youtube.com/watch?v=KL1MIuBfWe0&pp=ygUJ7YyM7J207I2s',790820,'1년 전'),('파이썬 무료 기초 강의 - 1강 파이썬이란 무엇인가?','https://www.youtube.com/watch?v=yytWGELNeOI&pp=ygUJ7YyM7J207I2s',662736,'2년 전'),('파이썬 무료 강의 100분 완성 (1분 파이썬 모음)','https://www.youtube.com/watch?v=T6z-0dpXPvU&pp=ygUJ7YyM7J207I2s',419581,'9개월 전'),('학교에서 안알려주는 파이값 계산하는 방법 (feat.파이썬)','https://www.youtube.com/watch?v=2WtouEmlLyY&pp=ygUJ7YyM7J207I2s',148437,'1개월 전'),('파이썬은 어디에 쓰일까?','https://www.youtube.com/watch?v=SzNFCim9nDE&pp=ygUJ7YyM7J207I2s',138927,'3년 전'),('아직도 파이썬을 이렇게 쓰고 있다구?','https://www.youtube.com/watch?v=fJeGAx27-vU&pp=ygUJ7YyM7J207I2s',115014,'5개월 전'),('파이썬으로 취업하기 어려운 이유','https://www.youtube.com/watch?v=PH2XhO-XyZw&pp=ygUJ7YyM7J207I2s',100399,'3년 전');
/*!40000 ALTER TABLE `python_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `react_videos`
--

DROP TABLE IF EXISTS `react_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `react_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `react_videos`
--

LOCK TABLES `react_videos` WRITE;
/*!40000 ALTER TABLE `react_videos` DISABLE KEYS */;
INSERT INTO `react_videos` VALUES ('React.js: The Documentary','https://www.youtube.com/watch?v=8pDqJVdNa44&pp=ygUIUmVhY3QuanM%3D',711501,'2개월 전'),('React & Node.js ИНТЕРНЕТ МАГАЗИН С НУЛЯ. PERN stack PostgreSQL + express + React js + node.js','https://www.youtube.com/watch?v=H2GCkRF9eko&pp=ygUIUmVhY3QuanM%3D',704278,'2년 전'),('React js full tutorial in Hindi | Complete Course','https://www.youtube.com/watch?v=GiyL4KFRNBA&pp=ygUIUmVhY3QuanM%3D',556350,'2년 전'),('¿Qué es React.js y cómo funciona? - La mejor explicación en español','https://www.youtube.com/watch?v=lWQ69WX7-hA&pp=ygUIUmVhY3QuanM%3D',421818,'3년 전'),('¿Qué es React.js y cómo funciona? - La mejor explicación en español','https://www.youtube.com/watch?v=lWQ69WX7-hA&pp=ygUIUmVhY3QuanM%3D',421818,'3년 전'),('Why React.js is taking a new direction','https://www.youtube.com/watch?v=1LkOa7Ky2ak&pp=ygUIUmVhY3QuanM%3D',347800,'3개월 전'),('Why React.js is taking a new direction','https://www.youtube.com/watch?v=1LkOa7Ky2ak&pp=ygUIUmVhY3QuanM%3D',347800,'3개월 전'),('React.js Full Course in Hindi for Beginners - 2023 | Master React in 12 Hours','https://www.youtube.com/watch?v=lLeZ8Cr2YVM&pp=ygUIUmVhY3QuanM%3D',234472,'4개월 전'),('React.js Full Course in Hindi for Beginners - 2023 | Master React in 12 Hours','https://www.youtube.com/watch?v=lLeZ8Cr2YVM&pp=ygUIUmVhY3QuanM%3D',234472,'4개월 전'),('ReactJS Full Course in 7 Hours | Learn React js | React.js Training | Edureka','https://www.youtube.com/watch?v=VyeA0tVreYw&pp=ygUIUmVhY3QuanM%3D',120577,'스트리밍 시간: 1년 전');
/*!40000 ALTER TABLE `react_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reactnative_videos`
--

DROP TABLE IF EXISTS `reactnative_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reactnative_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reactnative_videos`
--

LOCK TABLES `reactnative_videos` WRITE;
/*!40000 ALTER TABLE `reactnative_videos` DISABLE KEYS */;
INSERT INTO `reactnative_videos` VALUES ('초보자를 위한 React Native 튜토리얼 - React Native 앱 빌드','https://www.youtube.com/watch?v=0-S5a0eXPoc&pp=ugMICgJrbxABGAHKBQxSZWFjdCBOYXRpdmU%3D',2518851,'2년 전'),('React Native vs Flutter - 둘 다 사용하여 동일한 채팅 앱을 만들었습니다.','https://www.youtube.com/watch?v=X8ipUgXH6jw&pp=ugMICgJrbxABGAHKBQxSZWFjdCBOYXRpdmU%3D',1382108,'1년 전'),('React Native Tutorial for Beginners - Crash Course 2020','https://www.youtube.com/watch?v=qSRrxpdMpVc&pp=ygUMUmVhY3QgTmF0aXZl',1180692,'3년 전'),('Top 3 reasons why you should learn React Native','https://www.youtube.com/shorts/JoqjbkSTz9Y',580416,'1년 전'),('React Native Crash Course for Beginners - Build 4 Apps in 14 Hours (Redux, Tailwind + More) [2023]','https://www.youtube.com/watch?v=AkEnidfZnCU&pp=ygUMUmVhY3QgTmF0aXZl',350941,'9개월 전'),('React Native Crash Course for Beginners - Build 4 Apps in 14 Hours (Redux, Tailwind + More) [2023]','https://www.youtube.com/watch?v=AkEnidfZnCU&pp=ygUMUmVhY3QgTmF0aXZl',350941,'9개월 전'),('How to build a smoothly animated ToDo app with React Native, Expo, Reanimated, NativeBase, and Moti','https://www.youtube.com/watch?v=k2h7usLLBhY&pp=ygUMUmVhY3QgTmF0aXZl',345665,'1년 전'),('? Build Uber Eats with React Native & YELP API | Redux | Firebase | Google API','https://www.youtube.com/watch?v=jmvbhuJXFow&pp=ygUMUmVhY3QgTmF0aXZl',311909,'스트리밍 시간: 1년 전'),('Курс React Native. Пишем Мобильное Приложение на JavaScript','https://www.youtube.com/watch?v=7KwtXNoYQEY&pp=ygUMUmVhY3QgTmF0aXZl',265670,'3년 전'),('Build and Deploy a React Native App | 2023 React Native Course Tutorial for Beginners','https://www.youtube.com/watch?v=mJ3bGvy0WAY&pp=ygUMUmVhY3QgTmF0aXZl',226836,'1개월 전');
/*!40000 ALTER TABLE `reactnative_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_videos`
--

DROP TABLE IF EXISTS `security_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_videos`
--

LOCK TABLES `security_videos` WRITE;
/*!40000 ALTER TABLE `security_videos` DISABLE KEYS */;
INSERT INTO `security_videos` VALUES ('정보보안학과 #shorts','https://www.youtube.com/shorts/heF5jOXyaUw',1474378,'1년 전'),('정보보안 전문기업 엔시큐어 회사소개 동영상','https://www.youtube.com/watch?v=dc6DuVBSOcg&pp=ygUM7KCV67O067O07JWI',211144,'2년 전'),('해킹 및 정보보안 공부 방법, 공부 순서 정리 (생기초부터 최신 논문 읽는 방법까지)','https://www.youtube.com/watch?v=HdhvWcn8JOo&pp=ygUM7KCV67O067O07JWI',91882,'3년 전'),('대도서관 잡쇼 - 정보보안전문가 이승진_#001','https://www.youtube.com/watch?v=8p8PrunvHOc&pp=ygUM7KCV67O067O07JWI',68360,'5년 전'),('정보보호전문가 정보보안전문가 연봉 공개!!','https://www.youtube.com/watch?v=10KFP5h2jQo&pp=ygUM7KCV67O067O07JWI',57732,'4년 전'),('[정보보안기사] 1장(시스템보안)','https://www.youtube.com/watch?v=W9Fksf2t-u0&pp=ygUM7KCV67O067O07JWI',54574,'9년 전'),('2021년도 개인정보보호 및 정보보안 교육 영상','https://www.youtube.com/watch?v=d1wivdb5KNI&pp=ygUM7KCV67O067O07JWI',49377,'1년 전'),('정보보안과 해킹 기초 강좌 1강 - 해킹과 보안 (Information Security Basic Tutorial #1)','https://www.youtube.com/watch?v=2WH_C9SmDw0&pp=ygUM7KCV67O067O07JWI',43087,'6년 전'),('정보보안 전문가를 도전하시는 모든 분들에게 보안쟁이가 꼭 하고 싶은 말이 있습니다.(학원, 국비지원, 스터디, 자기개발)','https://www.youtube.com/watch?v=-FXrIDQKoEg&pp=ygUM7KCV67O067O07JWI',34537,'3년 전'),('[정보보안, 인공지능] 2022 Dreams Come True 웨비나 - 2/23(수)~24(목)','https://www.youtube.com/watch?v=aOpv-Iyktg8&pp=ygUM7KCV67O067O07JWI',31130,'1년 전');
/*!40000 ALTER TABLE `security_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `springboot_videos`
--

DROP TABLE IF EXISTS `springboot_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `springboot_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `springboot_videos`
--

LOCK TABLES `springboot_videos` WRITE;
/*!40000 ALTER TABLE `springboot_videos` DISABLE KEYS */;
INSERT INTO `springboot_videos` VALUES ('10시간 동안 5개의 Spring Boot 프로젝트 - 라인별 코딩 ?','https://www.youtube.com/watch?v=VR1zoNomG3w&pp=ugMICgJrbxABGAHKBQtTcHJpbmcgQm9vdA%3D%3D',639676,'1년 전'),('Spring Boot Complete Tutorial - 마스터 클래스','https://www.youtube.com/watch?v=zvR-Oif_nxg&pp=ugMICgJrbxABGAHKBQtTcHJpbmcgQm9vdA%3D%3D',550909,'1년 전'),('Introduction to Spring Boot | What is Spring Boot | Spring Boot Tutorial in Hindi','https://www.youtube.com/watch?v=729Pd-ZQ4uA&pp=ygULU3ByaW5nIEJvb3Q%3D',544977,'2년 전'),('Spring Boot Tutorial | Full In-depth Course','https://www.youtube.com/watch?v=c3gKseNAs9w&pp=ygULU3ByaW5nIEJvb3Q%3D',413217,'1년 전'),('Full Stack Development with Java Spring Boot, React, and MongoDB – Full Course','https://www.youtube.com/watch?v=5PdEmeopJVQ&pp=ygULU3ByaW5nIEJvb3Q%3D',304264,'3개월 전'),('Spring Boot Microservice Project Full Course in 6 Hours ???','https://www.youtube.com/watch?v=mPPhcU7oWDU&pp=ygULU3ByaW5nIEJvb3Q%3D',237404,'4개월 전'),('Spring Boot Microservice Project Full Course in 6 Hours ???','https://www.youtube.com/watch?v=mPPhcU7oWDU&pp=ygULU3ByaW5nIEJvb3Q%3D',237404,'4개월 전'),('Spring Boot 3 + Spring Security 6 - JWT Authentication and Authorisation [NEW] [2023]','https://www.youtube.com/watch?v=KxqlJblhzfI&pp=ygULU3ByaW5nIEJvb3Q%3D',230962,'4개월 전'),('Seu primeiro projeto Java web no Spring Boot','https://www.youtube.com/watch?v=D4frmIHAxEY&pp=ygULU3ByaW5nIEJvb3Q%3D',208878,'1년 전'),('Spring Boot - Learn Spring Boot 3 (2 Hours)','https://www.youtube.com/watch?v=-mwpoE0x0JQ&pp=ygULU3ByaW5nIEJvb3Q%3D',157086,'5개월 전');
/*!40000 ALTER TABLE `springboot_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `springframework_videos`
--

DROP TABLE IF EXISTS `springframework_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `springframework_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `springframework_videos`
--

LOCK TABLES `springframework_videos` WRITE;
/*!40000 ALTER TABLE `springframework_videos` DISABLE KEYS */;
INSERT INTO `springframework_videos` VALUES ('스프링 프레임워크 강의 1강 - Spring 소개와 학습 안내','https://www.youtube.com/watch?v=XtXHIDnzS9c&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',163875,'3년 전'),('스프링 프레임워크 강의 2강 - 느슨한 결합력과 인터페이스','https://www.youtube.com/watch?v=KJ9Rus3QfUc&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',59241,'3년 전'),('스프링 프레임워크 강의 3강 - DI(Dependency Injection)','https://www.youtube.com/watch?v=WjsDN_aFfyw&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',54881,'3년 전'),('스프링 프레임워크 강의 4강 - IoC(Inversion Of Control) 컨테이너','https://www.youtube.com/watch?v=QrIp5zc6Bo4&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',47189,'3년 전'),('스프링 프레임워크 강의 7강 - 스프링 DI 지시서 작성하기(Spring Bean Configuration)','https://www.youtube.com/watch?v=bYu9MNLBvX0&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',39133,'3년 전'),('스프링 프레임워크 강의 6강 - 스프링 DI 설정을 위해 이클립스 플러그인 설치하기','https://www.youtube.com/watch?v=Jwoz4ORX60A&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',38486,'3년 전'),('스프링 프레임워크 강의 8강 - 스프링 IoC 컨테이너 사용하기(ApplicationContext 이용하기)','https://www.youtube.com/watch?v=R_6fW1tVj8Y&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',36402,'3년 전'),('스프링 프레임워크 강의 12강 - 어노테이션을 이용할 때의 장점과 @Autowired를 이용한 DI 해보기','https://www.youtube.com/watch?v=S065KRjXRSY&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',28415,'3년 전'),('스프링 프레임워크 Part2 AOP 강좌 01강 - AOP(Aspect Oriented Programming) 이란?','https://www.youtube.com/watch?v=y2JkXjOocZ4&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',26010,'3년 전'),('스프링 프레임워크 강의 9강 - 값 형식 DI','https://www.youtube.com/watch?v=9iNvs7aeeDM&pp=ygUZ7Iqk7ZSE66eBIO2UhOugiOyehOybjO2BrA%3D%3D',24447,'3년 전');
/*!40000 ALTER TABLE `springframework_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sql_videos`
--

DROP TABLE IF EXISTS `sql_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sql_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sql_videos`
--

LOCK TABLES `sql_videos` WRITE;
/*!40000 ALTER TABLE `sql_videos` DISABLE KEYS */;
INSERT INTO `sql_videos` VALUES ('SQL Tutorial - Full Database Course for Beginners','https://www.youtube.com/watch?v=HXV3zeQKqGY&pp=ygUDU1FM',15206132,'4년 전'),('SQL Tutorial - Full Database Course for Beginners','https://www.youtube.com/watch?v=HXV3zeQKqGY&pp=ygUDU1FM',15206132,'4년 전'),('초보자를 위한 MySQL 자습서 [전체 과정]','https://www.youtube.com/watch?v=7S_tz1z_5bA&pp=ugMICgJrbxABGAHKBQNTUUw%3D',9207284,'4년 전'),('아직도 SQL을 모른다고해서 5분 설명해드림','https://www.youtube.com/watch?v=z9chRlD1tec&pp=ygUDU1FM',439276,'3년 전'),('MySQL Full Course for free ? (2023)','https://www.youtube.com/watch?v=5OdVJbNCSso&pp=ygUDU1FM',351793,'4개월 전'),('MySQL 데이터베이스 한번에 끝내기 SQL Full Tutorial Course using MySQL Database','https://www.youtube.com/watch?v=vgIc4ctNFbc&pp=ygUDU1FM',209857,'4년 전'),('왕초보용! 갖고 노는 MySQL 데이터베이스 강좌','https://www.youtube.com/watch?v=dgpBXNa9vJc&pp=ygUDU1FM',110703,'1년 전'),('SQL 배워서 일잘러로 거듭나자! l 4주만에 SQL 배우기','https://www.youtube.com/watch?v=efSVVbiZ1e4&pp=ygUDU1FM',102343,'2년 전'),('비전공자를 위한 SQL 입문서! | 쉽게 배우는 SQL! | 에어클래스','https://www.youtube.com/watch?v=MJsOoA8yM7A&pp=ygUDU1FM',61219,'3년 전'),('SQL 초보자가 꼭  알아야 하는 10가지 문법. 무료 강의. 편안하게 들어보세요','https://www.youtube.com/watch?v=ZsYnTSSuSiw&pp=ygUDU1FM',44001,'2년 전');
/*!40000 ALTER TABLE `sql_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vue_videos`
--

DROP TABLE IF EXISTS `vue_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vue_videos` (
  `title` text COLLATE utf8mb4_unicode_ci,
  `url` text COLLATE utf8mb4_unicode_ci,
  `view` int DEFAULT NULL,
  `date` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vue_videos`
--

LOCK TABLES `vue_videos` WRITE;
/*!40000 ALTER TABLE `vue_videos` DISABLE KEYS */;
INSERT INTO `vue_videos` VALUES ('Vue.js: The Documentary','https://www.youtube.com/watch?v=OrxmtDw4pVI&pp=ygUGVnVlLmpz',1458873,'3년 전'),('Уроки VUE.JS учим за 1 час для начинающих (Основы с нуля Vue js)  + небольшой обзор и сравнение','https://www.youtube.com/watch?v=b6Ac0jcqJIg&pp=ygUGVnVlLmpz',266131,'4년 전'),('한시간만에 끝내는 Vue.js 입문','https://www.youtube.com/watch?v=sqH0u8wN4Rs&pp=ygUGVnVlLmpz',130869,'2년 전'),('Vue.js (O competidor de peso do Angular e React) // Dicionário do Programador','https://www.youtube.com/watch?v=bEl6yN3vd-U&pp=ygUGVnVlLmpz',69014,'2년 전'),('Vue.js Tutorial: Beginner to Front-End Developer','https://www.youtube.com/watch?v=1GNsWa_EZdw&pp=ygUGVnVlLmpz',57673,'3개월 전'),('Vue.js/React/입문자도 이해하기 쉬운 명쾌한 비교','https://www.youtube.com/watch?v=W8uxLdeev7s&pp=ygUGVnVlLmpz',38354,'2년 전'),('[Vue.js로 게시판 만들기] 1. Create와 Read기능 만들기','https://www.youtube.com/watch?v=yX0bB9-Rzbw&pp=ygUGVnVlLmpz',21720,'4년 전'),('Vue js - 초보 입문 강좌 #1. 뷰? ,개발환경 준비','https://www.youtube.com/watch?v=DmgAvJhK3YE&pp=ygUGVnVlLmpz',20956,'2년 전'),('저는 Vue.js와 Axios를 이렇게 사용합니다. #1. Axios 모듈화','https://www.youtube.com/watch?v=bltYcZHCRk0&pp=ygUGVnVlLmpz',14849,'2년 전'),('저는 Vue.js와 Axios를 이렇게 사용합니다. #1. Axios 모듈화','https://www.youtube.com/watch?v=bltYcZHCRk0&pp=ygUGVnVlLmpz',14849,'2년 전');
/*!40000 ALTER TABLE `vue_videos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-26 22:24:29
