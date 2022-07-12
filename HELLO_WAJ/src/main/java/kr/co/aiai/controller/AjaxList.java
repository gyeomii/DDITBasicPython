package kr.co.aiai.controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.util.AjaxUtil;
import kr.or.aiai.dao.DaoEmp;
import kr.or.aiai.dao.EmpVO;

@WebServlet("/ajaxlist")
public class AjaxList extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public AjaxList() {
        super();
        // TODO Auto-generated constructor stub
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		DaoEmp de = new DaoEmp();
		ArrayList<EmpVO> list = null;
		try {
			list = de.getList();
			AjaxUtil.responseJson(response, list);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
