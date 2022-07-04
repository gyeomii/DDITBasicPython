<%@page import="kr.or.aiai.dao.EmpVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<!-- <script src="../js/jquery-3.6.0.min.js"></script> -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<title>Insert title here</title>
<style>
tr, th, td{
font-size: 1.5em;
text-align: center;
}
</style>
</head>
<body>
	<%
	EmpVO vo = (EmpVO) request.getAttribute("vo");
	%>
	<div class="col-md-6">
	<table class="table table-bordered">
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
	</table>
	<input type="button" class="btn btn-success" value="목록" onclick="location.href='emp_list'">
	<input type="button" class="btn btn-warning" value="수정" onclick="location.href='emp_mod'">
	<input type="button" class="btn btn-danger"value="삭제" onclick="location.href='emp_del'">
	</div>
</body>
</html>