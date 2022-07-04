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
		DaoEmp de = new DaoEmp();
		EmpVO vo = (EmpVO) request.getAttribute("pvo");
		int cnt = 0;
		try {
			cnt = de.insertEmp(vo);
		} catch (Exception e) {
			e.printStackTrace();
		}
		String msg = "";
		if(cnt > 0) {
			msg += "데이터 수정 성공";
		}else {
			msg += "데이터 수정 성공";
			
		}
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_mod_acts.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
