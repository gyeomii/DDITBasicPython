<%@page import="kr.or.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
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
	ArrayList<EmpVO> list = (ArrayList<EmpVO>) request.getAttribute("list");
%>
<table border="1px">
	<tr>
		<th>사번</th>
		<th>이름</th>
		<th>성별</th>
		<th>주소</th>
	</tr>
<%for(int i = 0; i < list.size(); i++){%>
<% EmpVO temp = (EmpVO)list.get(i); %>
	<tr>
		<td><%=temp.getE_id()%></td>
		<td><%=temp.getE_name()%></td>
		<td><%=temp.getSex()%></td>
		<td><%=temp.getAddr()%></td>
	</tr>
<%}%>
</body>
</html>