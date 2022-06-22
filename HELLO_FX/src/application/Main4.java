package application;

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

public class Main4 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tf;
	TextArea ta;

	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main4.fxml"));
			scene = new Scene(root, 250, 350); //(width, height)
			btn = (Button) scene.lookup("#btn");
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					multiple();
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void multiple() {
		int n = Integer.parseInt(tf.getText());
		String txt = "";
		for (int i = 1; i < 10; i++) {
			txt += (n + " * " + i + " =" + n * i + "\n");
		}
		ta.setText(txt);
	}

	public static void main(String[] args) {
		launch(args);
	}
}
