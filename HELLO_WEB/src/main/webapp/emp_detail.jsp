<%@page import="kr.or.aiai.dao.EmpVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
	EmpVO vo = (EmpVO) request.getAttribute("vo");
	%>
	<table border="1px">
		<tr>
			<th>사번</th>
			<td><%=vo.getE_id()%></a></td>
		</tr>
		<tr>
			<th>이름</th>
			<td><%=vo.getE_name()%></td>
		</tr>
		<tr>
			<th>성별</th>
			<td><%=vo.getSex()%></td>
		</tr>
		<tr>
			<th>주소</th>
			<td><%=vo.getAddr()%></td>
		</tr>
</body>
</html>