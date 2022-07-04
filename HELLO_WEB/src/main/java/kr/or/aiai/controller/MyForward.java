package kr.or.aiai.controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.or.aiai.dao.EmpVO;

/**
 * Servlet implementation class MyForward
 */
@WebServlet("/myforward")
public class MyForward extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public MyForward() {
		super();
		// TODO Auto-generated constructor stub
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		
		String a = "999";
		request.setAttribute("a", a);
		
		ArrayList<EmpVO> list = new ArrayList<EmpVO>();
		list.add(new EmpVO("1", "1", "1", "1"));
		list.add(new EmpVO("2", "2", "2", "2"));
		request.setAttribute("list", list);
		
		RequestDispatcher rd = request.getRequestDispatcher("/myforward.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
