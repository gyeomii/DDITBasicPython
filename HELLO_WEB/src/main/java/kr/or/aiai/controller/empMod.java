package kr.or.aiai.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.or.aiai.dao.DaoEmp;
import kr.or.aiai.dao.EmpVO;

@WebServlet("/emp_mod")
public class empMod extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public empMod() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		String e_id = request.getParameter("e_id");
		DaoEmp de = new DaoEmp();
		EmpVO vo = null;

		try {
			vo = de.getOne(e_id);
			request.setAttribute("vo", vo);
		} catch (Exception e) {
			e.printStackTrace();
		}

		RequestDispatcher rd = request.getRequestDispatcher("/emp_detail.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
