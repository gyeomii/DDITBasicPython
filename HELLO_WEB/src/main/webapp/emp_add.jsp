<%@page import="kr.or.aiai.dao.EmpVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- BS CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<title>Insert title here</title>
</head>
<body>
<%
String msg = (String) request.getAttribute("msg");
if(msg==null){
	msg = "";
}else{
	msg = (String) request.getAttribute("msg");
}
%>
	<form action="emp_add">
		<label>사번 : <input type="text" name="e_id"/></label><br>
		<label>이름 : <input type="text" name="e_name"/></label><br>
		<label>성별 : <input type="text" name="sex"/></label><br>
		<label>주소 : <input type="text" name="addr"/></label><br>
		<input type="submit" value="실행">
		<p><%=msg %></p>
	</form>	
		<input type="button" value="메인으로 돌아가기" onclick="location.href='emp_list'">
</body>
</html>