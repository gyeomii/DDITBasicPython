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

@WebServlet("/emp_mod_acts")
public class empModActs extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public empModActs() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String e_id = request.getParameter("e_id");
		String e_name = request.getParameter("e_name");
		String sex = request.getParameter("sex");
		String addr = request.getParameter("addr");
		
		System.out.println("e_id:"+e_id);
		System.out.println("e_name:"+e_name);
		System.out.println("sex:"+sex);
		System.out.println("addr:"+addr);
		
		DaoEmp de = new DaoEmp();
		int cnt = -1;
		try {
			cnt = de.updateEmp(new EmpVO(e_id, e_name, sex, addr));
		} catch (Exception e) {
			e.printStackTrace();
		}
		request.setAttribute("cnt", cnt); 
		System.out.println("cnt:"+cnt);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_mod_acts.jsp");
		rd.forward(request,response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		doGet(request, response);
	}

}
