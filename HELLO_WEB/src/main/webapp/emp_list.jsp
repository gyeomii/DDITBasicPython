<%@page import="kr.or.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
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
	ArrayList<EmpVO> list = (ArrayList<EmpVO>) request.getAttribute("list");
	%>
	<table border="1px">
		<tr>
			<th>사번</th>
			<th>이름</th>
			<th>성별</th>
			<th>주소</th>
		</tr>
		<%
		for (int i = 0; i < list.size(); i++) {
		%>
		<%
		EmpVO temp = (EmpVO) list.get(i);
		%>
		<tr>
			<td><a href="emp_detail?e_id=<%=temp.getE_id()%>"><%=temp.getE_id()%></a></td>
			<td><%=temp.getE_name()%></td>
			<td><%=temp.getSex()%></td>
			<td><%=temp.getAddr()%></td>
		</tr>
		<%
		}
		%>
		</table>
<input type="button" id="add" value="추가" onclick="location.href='./emp_add.jsp'"/>

</body>
</html>