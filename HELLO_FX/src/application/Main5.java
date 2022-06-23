package application;

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main5 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tf_user;
	TextField tf_com;
	TextField tf_result;
	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main5.fxml"));
			scene = new Scene(root, 250, 350); //(width, height)
			btn = (Button) scene.lookup("#btn");
			tf_user = (TextField) scene.lookup("#tf_user");
			tf_com = (TextField) scene.lookup("#tf_com");
			tf_result = (TextField) scene.lookup("#tf_result");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					EvenOdd();
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void EvenOdd() {
		String user = tf_user.getText();
		String com = ComRandom();
		String result ="";
		tf_com.setText(com);
		if(user.equals(com)) {
			result = "User 승리";
		}else {
			result = "COM 승리";
		}
		tf_result.setText(result);
	}
	
	public String ComRandom() {
		String com = "";
		Random rnd = new Random();
		int n = rnd.nextInt(2);
		if(n == 1) {
			com = "홀";
		}else {
			com = "짝";
		}
		return com;
	}
	public static void main(String[] args) {
		launch(args);
	}
}